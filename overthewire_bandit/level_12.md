# Description
The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work. Use mkdir with a hard to guess directory name. Or better, use the command “mktemp -d”. Then copy the datafile using cp, and rename it using mv (read the manpages!)

Hexdumps are often used when we want to look at data that cannot be represented in strings and therefore is not readable, so it is easier to look at the hex values. A hexdump has three main columns. The first shows the address, the second the hex representation of the data on that address and the last shows the actual data as strings

For the command line xxd can be used. xxd <input_file> <output_file> creates hexdumps. When using the -r flag, it reverts the hexdump.

- gzip is a command to compress or decompress (-d) files. A ‘gzip’ file generally ends with .gz.
- bzip2 is another command which allows for compressing and decompressing (-d) files. A ‘bzip2’ file generally ends with .bz2.

- An Archive File is a file that contains one or multiple files and their metadata. This can allow easier portability.
- tar is a command that creates archive files (-cf). It also allows extracting these files again (-xf). A tar archive generally ends with .tar.

# Solution

```sh
cd /tmp
mktemp -d
cd /tmp/tmp.W5t1vua6G9
cp ~/data.txt
mv data.txt hexdump_data
cat hexdump_data
```

However, we want to operate on the actual data. Therefore, we revert the hexdump and get the actual data.
```sh
xxd -r hexdump_data compressed_data
```

Repeatedly decompress
```sh
cat hexdump_data
```

| **Format**                  | **Magic Number (Hex)**    | **Magic Number (ASCII / Description)**                               |
| --------------------------- | ------------------------- | -------------------------------------------------------------------- |
| **GZIP** (`.gz`)            | `1F 8B 08`                | Standard GZIP header                                                 |
| **BZIP2** (`.bz2`)          | `42 5A 68`                | ASCII: `BZh`                                                         |
| **XZ** (`.xz`)              | `FD 37 7A 58 5A 00`       | Identifies the XZ format                                             |
| **LZMA (Alone)**            | `5D 00 00`                | Legacy LZMA format                                                   |
| **Zstandard** (`.zst`)      | `28 B5 2F FD`             | Zstandard magic number                                               |
| **ZIP** (`.zip`)            | `50 4B 03 04`             | ASCII: `PK..` (also: `50 4B 05 06` or `50 4B 07 08` for end records) |
| **RAR (v1.5 - v4.x)**       | `52 61 72 21 1A 07 00`    | ASCII: `Rar!`                                                        |
| **RAR (v5.x)**              | `52 61 72 21 1A 07 01 00` | Updated RAR format                                                   |
| **7-Zip** (`.7z`)           | `37 7A BC AF 27 1C`       | Unique 7z identifier                                                 |
| **ARJ** (`.arj`)            | `60 EA`                   | Used in older ARJ archives                                           |
| **LZH / LHA** (`.lzh`)      | `2D 6C 68`                | ASCII: `-lh` (common in old LZH formats)                             |
| **CAB (Microsoft Cabinet)** | `4D 53 43 46`             | ASCII: `MSCF`                                                        |

```sh
mv compressed_data compressed_data.gz
```

Do this for bunzip and gzip.and then unarchive with tar
```sh
mv compressed_data compressed_data.tar
tar -xf compressed_data.tar
xxd data8.bin
mv data8.bin data8.gz
gzip -d data8.gz
cat data8
```

[Next Level](level_13.md)

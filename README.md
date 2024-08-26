# otp (one time pad)

## Description

otp_python creates five small programs that encrypt and decrpyt information similar to a one-time pad-like system. Focuses is using inter-process communication, UNIX features such as input/output and redirection and job control.

A one-time pad-like system is an enryption technique that cannot be cracked and requires the use of a pre-shared key. To work, the plaintext is paired with the key (aka one-time pad). Each character of the plaintext is encrypted by combining it with the corresponding character of the same index position from the key using modular addition.

This same system is also used to decrpyt a message.

Three key definitions are important:

**Plaintext**: term for the information to be encrypted or decrypted and is human readable. 

**Ciphertext**: term for resultant output of encrpytion and decryption. It is not human readable and cannot be cracked.

**Key**: the random sequence of characters that will be used to convert the plaintext to ciphertext and vice versa.

## How to Compile

Compile by typing python3 otp_python.py with the following combinations of commands and flags below

## Usage

```shell
usage: otp [--version] [--help] [--verbose [VERBOSE]]
        keygen [--length LENGTH] [--seed [SEED]] |
        encode [--in-file [PT-FILE] | --text PT-STRING] [--out-file CT-FILE] 
            --key-file KEY-FILE | 
        decode [--in-file [CT-FILE] | --text CT-STRING] [--out-file PT-FILE] 
            --key-file KEY-FILE |
```

|    cmd   | short name | option/arg                | description                                   | type      |
| -------- | -----------| --------------------------|---------------------------------------------- | --------- |
| `otp`    |            |                           |                                               |           |
|          |            | `--version`:              | Show program's version number                 | BOOL      |
|          |            | `--help`                  | Show help message                             | BOOL      |
|          | `-v`       | `--verbose[=VERBOSE]`     | Set verbosity level                           | COUNTER   |
| `keygen` |            |                           |                                               |           |
|          | `-l`       | `--length=LENGTH`         | Specify length of the key                     | INTEGER   |
|          | `-s`       | `--seed[=SEED]`           | Specify seed for key generation               | INTEGER   |
| `encode` |            |                           |                                               |           |
|          | `-i`       | `--in-file[=PT-FILE]`     | Specify input file for encoding               | FILENAME  |
|          | `-t`       | `--text=PT-STRING`        | Specify input text directly for encoding      | STRING    |
|          | `-o`       | `--out-file[=CT-FILE]`    | Specify output file                           | FILENAME  |
|          | `-k`       | `--key-file=KEY-FILE`     | Specify key file                              | FILENAME  |
| `decode` |            |                           |                                               |           |
|          | `-i`       | `--in-file[=CT-FILE]`     | Specify input file for decoding               | FILENAME  |
|          | `-t`       | `--text=CT-STRING`        | Specify input text directly for decoding      | STRING    |
|          | `-o`       | `--out-file[=PT-FILE]`    | Specify output file                           | FILENAME  |
|          | `-k`       | `--key-file=KEY-FILE`     | Specify key file                              | FILENAME  |

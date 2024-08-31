# Encryption and Decryption Techniques

## Overview

This project includes two Python scripts for basic encryption and decryption:

- **Caesar Cipher**: Shifts each letter in the plaintext by a fixed number of positions.
- **Substitution Cipher**: Substitutes characters based on a shuffled key for more complex encryption.

## Features

- **Caesar Cipher**: Encrypt and decrypt messages using a shift value.
- **Substitution Cipher**: Encrypt and decrypt messages using a shuffled key.

## Prerequisites

- **Python 3.x**

## Example

**Caesar Cipher**:
```bash

python caesar_cipher.py encrypt "hello" --key 3
# Output: khoor

python caesar_cipher.py decrypt "khoor" --key 3
# Output: hello


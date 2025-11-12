# Caese Cipher Encryption / Decryption

[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/)
[![Last Commit](https://img.shields.io/github/last-commit/twinodev/Caese_Cipher_Encryption_Decryption.svg)](https://github.com/twinodev/Caese_Cipher_Encryption_Decryption/commits/main)
[![GitHub Repo stars](https://img.shields.io/github/stars/twinodev/Caese_Cipher_Encryption_Decryption.svg?style=social)](https://github.com/twinodev/Caese_Cipher_Encryption_Decryption/stargazers)
[![Issues](https://img.shields.io/github/issues/twinodev/Caese_Cipher_Encryption_Decryption.svg)](https://github.com/twinodev/Caese_Cipher_Encryption_Decryption/issues)

[<img src="./assets/logo.png" alt="Twinodev" width="64">![TwinoDev]](https://github.com/twinodev)


A simple command-line Python implementation of a Caesar-style cipher that lets you encrypt and decrypt messages.

This repository contains a small interactive script (`caese_cipher.py`) that demonstrates a character-shifting cipher over a custom character set (letters, digits, punctuation and space). The project is intended as a learning example for basic encryption logic and Python I/O.

## Features

- Interactive CLI to encrypt or decrypt a message
- Supports letters (upper/lower), digits, punctuation and space
- Produces an "unlock key" during encryption that is required for decryption

## Files

- `caese_cipher.py` — main Python script (interactive). Run directly with Python 3.
- `LICENSE` — MIT License for this project

## Requirements

- Python 3.7+ (should work with most modern Python 3.x releases)

## Installation

No external dependencies. Clone the repo and run the script with Python:

```powershell
python .\caese_cipher.py
```

On Windows PowerShell, use the command above from the repository directory.

## Usage

When you run `caese_cipher.py` it shows a small menu:

1. Encrypt Message
2. Decrypt Message

Choose `1` to encrypt or `2` to decrypt and follow prompts.

Encryption flow (interactive):

- The script asks for a message to be encrypted.
- It asks for an encryption key (a 4-digit numeric value). The script multiplies that key by the message length to produce an "unlock key" which is shown after encryption — you must supply this unlock key when decrypting.

Example (encrypt):

```
Welcome TwinoDev Caesar Cipher Master.

1.Encrypt Message
2.Decrypt Message
Enter a mode: 1
Enter a message to be encrypted: Hello, World!
Enter an lock key: 1234
Your encrypted message is: <ciphertext>
Unlock key is: 1234 * 13 = 16042
```

Example (decrypt):

```
Welcome TwinoDev Caesar Cipher Master.

1.Encrypt Message
2.Decrypt Message
Enter a mode: 2
Enter a cipher text: <ciphertext>
Enter unlock key: 16042
Your original message is: Hello, World!
```

Notes about the implementation

- The script uses a custom `keys` string equal to letters (both cases), digits, punctuation and space.
- The encryption `shift` is supplied by the user (must be 4 digits long in the current script). The program multiplies that shift by the message length to produce the unlock key.
- The implementation is primarily educational. It is not secure for real-world use.

Known quirks and suggestions

- The script requires a 4-digit key for encryption and expects the unlock key to be a number derived from that key; these checks and calculations are hard-coded in `caese_cipher.py`.
- There are some validation checks in the script that can be improved (for example, clearer error messages and edge-case handling for empty messages). Also, `shift` is converted from a string and used arithmetically — if you want arbitrary integer shifts you can relax the 4-digit constraint.
- If you'd like a safer or standardized cipher, consider using well-known libraries (for example, the `cryptography` package) rather than rolling your own.

## Contributing

Contributions are welcome. If you want to improve the script:

1. Fork the repository
2. Create a branch for your change
3. Make your changes and add tests (if applicable)
4. Submit a pull request describing the change

Suggested small improvements:

- Add unit tests for encryption/decryption pairs
- Add a command-line argument mode (so the script can be used non-interactively)
- Improve input validation and error messages

## License

This project is licensed under the MIT License — see the included `LICENSE` file for details.

## Author

Twinomujuni Emmanuel

---


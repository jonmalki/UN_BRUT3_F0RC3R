# UN_BRUT3_F0RC3R

This is a Python script that generates highly secure passwords and hashes them using the Argon2 hashing algorithm.

## Purpose

The purpose of this script is to provide a simple and secure way to generate and hash passwords for use in various applications, such as user authentication or password storage.

## Requirements

To run this script, you will need:

- Python 3.x
- `argon2-cffi` library: can be installed via pip with `pip install argon2-cffi`
- `termcolor2` library: can be installed via pip with `pip install termcolor2`

## Usage

To use this script, follow these steps:

1. Download or clone the script from the [GitHub repository](https://github.com/jonmalki/UN_BRUT3_F0RC3R).
2. Install the required libraries using pip (`argon2-cffi` and `termcolor2`).
3. Run the script using the command `python un_brut3_f0rc3r.py`.
4. The script will generate a secure password and print its hash to the console.
5. The final hashed password will also be printed for storage or comparison.

## Customization

The script allows for customization of several parameters to suit your needs, including:

- Password length: You can adjust the `password_length` variable in the script to generate longer or shorter passwords.
- Character set: The `all_chars` variable in the script can be modified to include or exclude certain characters.
- Salt: The script generates a random salt for each password, but you can change the salt length or value by modifying the `salt` variable.
- Number of threads: The `num_threads` variable controls the number of threads used for password generation and hashing.

## Security

This script uses a combination of the `scrypt` key derivation function and the Argon2 hashing algorithm to generate and hash passwords. These algorithms are designed to be highly secure and resistant to brute-force attacks. The script also uses a random salt for each password, which makes it harder for attackers to precompute hashes.

## Contributing

Contributions to this project are welcome. If you find any bugs or have suggestions for improvements, please create an issue or submit a pull request on the [GitHub repository](https://github.com/jonmalki/UN_BRUT3_F0RC3R).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

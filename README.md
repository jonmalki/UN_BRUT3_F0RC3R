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

This script uses a combination of the `scrypt` key derivation function and the Argon2 hashing algorithm to generate and hash passwords. Scrypt is a key derivation function that uses a large amount of memory, making it difficult for attackers to use GPUs or ASICs to crack the hash. Argon2 is the winner of the Password Hashing Competition in 2015 and is considered one of the most secure password hashing algorithms available.

In addition to these features, the script also uses a random salt for each password, which makes it harder for attackers to precompute hashes. The script also slows down the password hashing process by using a sleep function. This ensures that the hashing process is resource-intensive and time-consuming, making it harder for attackers to crack the hash. The number of threads used for password generation and hashing can also be configured, further increasing the security of the passwords generated.

Another security feature of this script is that it uses the `argon2-cffi` library to hash passwords. This library is a Python wrapper for the C implementation of Argon2, which is faster and more secure than the pure Python implementation.

Overall, the combination of Scrypt, Argon2, random salts, sleep functions, and the `argon2-cffi` library makes this script highly secure and resistant to brute-force attacks.

## Quantum resistance

Argon2 is currently believed to be quantum-resistant, meaning that it is unlikely to be broken by a quantum computer. However, this is a rapidly evolving field of research, and it is possible that quantum computers may become more powerful in the future and be able to break Argon2. Currently, it is estimated that a quantum computer with 1000 qubits would take approximately 2^64 operations to break a 256-bit Argon2 hash. This would take about 3.4 x 10^19 years using a classical computer, and about 3.4 million years (3,400,000) using a quantum computer with 1000 qubits. To put this in perspective, the estimated age of the universe is about 13.8 billion years. So even with a quantum computer, it would take many times longer than the current age of the universe to break a 256-bit Argon2 hash. Therefore, it is safe to say that using Argon2 to hash passwords is currently a highly secure practice.

## Contributing

Contributions to this project are welcome. If you find any bugs or have suggestions for improvements, please create an issue or submit a pull request on the GitHub repository.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

#UN_BRUT3_F0RC3R

This is a Python script that generates highly secure passwords and hashes them using the Argon2 hashing algorithm. The script uses a combination of the scrypt key derivation function and a randomly generated salt to derive secure passwords from an initial password string. The derived password is then hashed using Argon2 to generate a secure hash of the password.

The password generation process is made even more secure and time-consuming by running multiple threads simultaneously. The number of threads used for password generation and hashing can be configured by changing the num_threads variable in the script.

#Requirements

Python 3.x
argon2-cffi library: can be installed via pip with pip install argon2-cffi
termcolor2 library: can be installed via pip with pip install termcolor2
#Usage

Download or clone the script from the GitHub repository.
Install the required libraries using pip (argon2-cffi and termcolor2).
Run the script using the command python un_brut3_f0rc3r.py.
The script will generate a secure password and print its hash to the console.
The final hashed password will also be printed for storage or comparison.
#Customization

The script allows for customization of password length, character set, salt, and number of threads used for password generation and hashing. These variables can be easily modified in the script to suit your needs.

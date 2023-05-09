import random
import string
import secrets
import hashlib
import time
import threading
import queue
import argon2
from termcolor2 import colored

# Define the password length and character set
password_length = 1280
all_chars = string.ascii_letters + string.digits + string.punctuation

# Generate a secure random salt
salt = secrets.token_bytes(16)

# Initialize variables for password and hash
password = ''
hashed_password = ''

# Define the number of threads to use
num_threads = 16

# Define a function to hash passwords using Argon2 and salting
def hash_password(password):
    # Combine the password and salt
    password_with_salt = password.encode() + salt

    # Hash the password using Argon2
    hashed_password = argon2.PasswordHasher().hash(password_with_salt)

    return hashed_password

# Define a function to generate secure passwords using scrypt and add them to the queue
def generate_secure_passwords(q):
    while True:
        # Generate a random password
        initial_password = ''.join(secrets.choice(all_chars) for i in range(password_length))

        # Derive a key from the initial password using scrypt with a high cost factor
        secure_password = hashlib.scrypt(initial_password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=128)

        # Print the generated secure password
        print(f"Generated secure password: {secure_password.hex()}")

        # Add the secure password to the queue
        q.put(secure_password)

# Define a function to hash passwords from the queue and add them to a set
def hash_passwords(q, password_set):
    while True:
        # Get a password from the queue
        password = q.get()

        # Hash the password and add it to the set
        hashed_password = hash_password(password)
        password_set.add(hashed_password)

        # Print the hashed password
        print(f"Hashed password: {hashed_password}")

        # Slow down the hashing to use more CPU time
        time.sleep(0.01)

        # Mark the task as complete
        q.task_done()

# Create a queue for generating passwords and a set for hashed passwords
password_queue = queue.Queue()
hashed_password_set = set()

# Start the secure password generation threads
password_threads = []
for i in range(num_threads):
    password_thread = threading.Thread(target=generate_secure_passwords, args=(password_queue,))
    password_thread.start()
    password_threads.append(password_thread)

# Start the password hashing threads
hash_threads = []
for i in range(num_threads):
    hash_thread = threading.Thread(target=hash_passwords, args=(password_queue, hashed_password_set))
    hash_thread.start()
    hash_threads.append(hash_thread)

# Wait for all passwords to be generated and hashed
password_queue.join()
for password_thread in password_threads:
    password_thread.join()

for hash_thread in hash_threads:
    hash_thread.join()

# Get the final hashed password from the set
hashed_password = hashed_password_set.pop()

# Print the salt in rainbow-colored text
print(colored(f"Salt: {salt.hex()}", "rainbow"))

# Print the final hashed password for storage or comparison
print(colored(f"Hashed Password: {hashed_password}", "rainbow"))

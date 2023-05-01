import random
import string

def generate_password(length):
    # Define the character sets to use in the password
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine the character sets into a single pool of characters
    pool = lowercase + uppercase + digits + symbols

    # Generate the password by randomly selecting characters from the pool
    password = ''.join(random.choice(pool) for i in range(length))
    return password

# Prompt the user for the desired length of the password
length = int(input("Enter the length of the password: "))

# Generate the password and print it to the console
password = generate_password(length)
print("Your random password is:", password)
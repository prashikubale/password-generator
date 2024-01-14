import random
import string

def generate_password(length):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password using random.choices
    password = ''.join(random.choices(characters, k=length))

    return password

# Get the desired password length from the user
try:
    length = int(input("Enter the desired password length: "))
    if length <= 0:
        raise ValueError("Password length must be greater than 0.")
except ValueError as e:
    print(f"Error: {e}")
    length = 12  # Set a default length if the input is invalid

# Generate and print the password
password = generate_password(length)
print(f"Generated Password: {password}")

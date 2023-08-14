import random

# Define the character set that you want to use for your passwords.
# For example, this set includes lowercase letters, uppercase letters, numbers, and symbols:

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+"

# Generate a random password of the specified length.
# The length of the password is specified by the `length` parameter.

def generate_password(length):
  password = ""
  for i in range(length):
    password += random.choice(characters)
  return password

# Print the generated password to the console.

print(generate_password(4))
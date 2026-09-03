import random
import string

letters = string.ascii_letters
numbers = string.digits
symbols = "!@#$%^&*"

all_characters = letters + numbers + symbols

length = int(input("Enter password length: "))

password = ""

for i in range(length):
    password += random.choice(all_characters)

print("Generated Password:", password)
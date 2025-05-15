import random
import string

def generate_password(length:int = 16):
    characters = string.ascii_letters + string.punctuation
    new_password = ''
    for character in characters:
        new_password += random.choice(characters)
    return new_password[:length]

print(generate_password())
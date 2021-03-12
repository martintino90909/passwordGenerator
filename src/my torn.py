import random
import string


def generate_password(length):
    password = ""
    for i in range(length):
        password += random.choice(string.ascii_lowercase)
    return password


default_length = 8
try:
    user_input = input('Please enter password length: ')
except:
    user_input = default_length

print(generate_password(user_input))
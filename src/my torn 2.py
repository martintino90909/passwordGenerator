import random
import string

default_length = 20


def generate_password(length):
    password = ""
    for i in range(length):
        password += random.choice(string.ascii_lowercase)
    return password


def get_password_content(password_composure):
    input('What would you like the password to made up of (l=Letters, d=Digits, p=Punctuation)')


def get_correct_user_input(message):
    while True:
        try:
            user_input = int(input(message) or default_length)
        except ValueError:
            print("Please enter a integer")
            continue
        else:
            break
    return user_input


msg = "Please enter password length [" + str(default_length) + "] : "
user_int_input = get_correct_user_input(msg)
output = generate_password(user_int_input)
print(output)

password_file = open('password.txt', 'a')
password_file.write(output + "\n")
password_file.close()

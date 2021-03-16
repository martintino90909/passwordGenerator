import random
import string
import pyAesCrypt

default_length = 20
password = "system"
bufferSize = 64 * 1024


def generate_password(length, uppercase, numbers, punctuation):
    password = ""
    selection_pool = string.ascii_lowercase
    if uppercase is True:
        selection_pool += string.ascii_uppercase
    if numbers is True:
        selection_pool += string.digits
    if punctuation is True:
        selection_pool += "!#@*%.,/?():;"
    for i in range(length):
        password += random.choice(selection_pool)
    return password


def get_correct_user_input(message):
    user_input = ""
    while True:
        try:
            user_input = int(input(message) or default_length)
        except ValueError:
            print("Please enter a integer")
            continue
        else:
            break
    return user_input


def get_correct_user_boolean(message, default_value):
    user_boolean_selection = input(message) or default_value
    if user_boolean_selection is default_value:
        return user_boolean_selection
    elif user_boolean_selection.lower() == "y" or user_boolean_selection.lower() == "yes":
        return True
    elif user_boolean_selection.lower() == "n" or user_boolean_selection.lower() == "no":
        return False
    else:
        print("Incorrect input please enter Y/N")
        return get_correct_user_boolean(message, default_value)


msg = "Please enter password length [" + str(default_length) + "] : "
user_int_input = get_correct_user_input(msg)

print("INFO:Lowercase is always enabled")

uppercase_message = "Would you like your password to contain upper case letters [Y] :"
use_uppercase = get_correct_user_boolean(uppercase_message, True)

digit_message = "Would you like your password to contain digits [Y] :"
use_digits = get_correct_user_boolean(digit_message, True)

special_message = "Would you like your password to contain special characters [Y] :"
use_special = get_correct_user_boolean(special_message, True)

print(use_uppercase, use_digits, use_special)


output = generate_password(user_int_input, use_uppercase, use_digits, use_special)
print(output)


password_file = open('password.txt', 'a')
password_file.write(output + "\n")
password_file.close()

#pyAesCrypt.decryptFile('secure_passwords.txt', 'password.txt', password, bufferSize)

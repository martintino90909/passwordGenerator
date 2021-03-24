import password_generation
import data_store

def main_menu():
    print('''1) Add credentials
2) Retrieve credentials''')
    user_selection = int(input("Enter selection :"))
    if user_selection == 1:
        add_credentials()
    elif user_selection == 2:
        retrieve_credentials()



def add_credentials():
    website_name = input("Website name :")
    user_name = input("Username :")
    password = input("Password [Leave blank to generate password] :")
    if password == "":
        password = password_generation.generate_password()
    data_store.add_password(website_name, user_name, password)
    main_menu()




def retrieve_credentials():
    print('''1)Use website name
2)Use username''')
    user_input = int(input("Enter selection :"))
    if user_input == 1:
        website_input = input("Website name :")
        print(data_store.get_password(website_input))
    elif user_input == 2:
        user_name = input("Username :")
        print(data_store.get_password_with_username(user_name))
    main_menu()
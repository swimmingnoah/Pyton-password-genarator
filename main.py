import random
import string



def password_input():
    website = input("What website you would like to create a new password for? ")
    email = input("What email would you like to use? ")
    while True:
        try:
            digit = int(input("How long would you like your password to be? "))
        except ValueError:
            print("Please enter an integer.")
            continue
        else:
            return digit
            break
    


def password_creator(digit):
    password_characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(password_characters)
                       for i in range(digit))

def password_print(website, email, password):
    print("\nYour password is:")
    print("\nWebsite: " + website)
    print("\nEmail: " + email)
    print("\nPassword: " + password)

def write_password():
    f = open("super_secret_passwords.txt", "r")
    f.write(digit)
    f.close()

def main():

    print("Welcome to the password generator!\n")
    print("1. Generate new password")
    print("2. View passwords")
    print("3. Quit")
    option_choice = int(input("Please enter a choice: "))

    if option_choice == 1:
        password_input()
        write_password()
        print(website)


    elif option_choice == 2:
        view_pass()

    else:
        print("please pick a number between 1 and 3")

main()
print(website)

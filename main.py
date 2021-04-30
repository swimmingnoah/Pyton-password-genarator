import random
import string
import csv


def password_input():
    website = input(
        "What website you would like to create a new password for? ")
    email = input("What email would you like to use? ")

    while True:
        try:
            digit = int(input("How long would you like your password to be? "))
            myTuple = (digit, website, email)
            return myTuple
        except ValueError:
            print("Please enter an integer.")
            continue


def password_creator(digit):
    password_characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(password_characters)
                       for i in range(digit))
    return password


def password_print(website, email, password):
    print("\nYour password is:")
    print("\nWebsite: " + website)
    print("\nEmail: " + email)
    print("\nPassword: " + password)


def write_password():
    f = open("super_secret_passwords.txt", "r")
    f.write(digit)
    f.close()


def writeItems(website, email, password):
    vault = 'super_secret_passwords.txt'
    headerList = ['Website', 'email', 'password']
    with open(vault, mode='a+') as vault:
        vault_writer = csv.writer(
            vault, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL,)
        vault_writer.writerow(
            ['Website: ' + website, ' Email: ' + email, ' Password: ' + password])


def readItems():
    with open('super_secret_passwords.txt', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(', '.join(row))


def main():

    print("Welcome to the password generator!\n")
    print("1. Generate new password")
    print("2. View passwords")
    print("3. Quit")
    option_choice = int(input("Please enter a choice: "))

    if option_choice == 1:
        x = password_input()
        digit = x[0]
        website = x[1]
        email = x[2]
        password = password_creator(x[0])
        password_print(website, email, password)
        writeItems(website, email, password)

    elif option_choice == 2:
        readItems()

    else:
        print("Thank you for using the password generator")


main()

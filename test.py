import random
import string

def password_creator(digit):
    password_characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(password_characters)
                       for i in range(digit))
    return password


print(password_creator(10))

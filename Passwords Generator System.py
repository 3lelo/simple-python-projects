from random import randint, choice, shuffle
import string

all_passwords = []

def generate_password(size):
    l_letters = randint(1,size - 3)

    size -= l_letters
    u_letters = randint(1,size - 2)

    size -= u_letters
    digits = randint(1,size - 1)

    size -= digits
    punctuation = size

    password = ''
    for i in range (l_letters):
        password += choice(string.ascii_lowercase)
    
    for i in range (u_letters):
        password += choice(string.ascii_uppercase)

    for i in range (digits):
        password += choice(string.digits)

    for i in range (punctuation):
        password += choice(string.punctuation)

    password = list(password)
    shuffle(password)

    password = ''.join(password)

    print (f"\nYour password is : {password}")

    all_passwords.append(password)

print ("Welcome to the Passwords Generator System\n")

size = input("Enter the size of the password (should be > 8 and < 20) or 'quit' to leave : ")
size = size.lower()

while size != 'quit':
    try:
        size = int(size)
        if size < 8 or size > 20:
            print ("\nYou're out of the range (size > 8 , size < 20)\n")

            size = input("Enter the size of the password (should be > 8 and < 20) or 'quit' to leave : ")
            size = size.lower()

            continue
        generate_password(size)

    except ValueError:
        print ("\nInvalid input! Please enter an int\n")

    size = input("Enter the size of the password (should be > 8 and < 20) or 'quit' to leave : ")
    size = size.lower()

if all_passwords:
    print ("\nYour generated passwords are : ")

    for password in all_passwords:
        print (f"- {password}")

    print ("\nThank you for using Passwords Generator System. Good bye ^_^")
else:
    print ("\nThere's no passwords :(")

contacts = {}
def menu():
    print ("Enter an option:")
    print ("1. Add a contact")
    print ("2. View all contacts")
    print ("3. Search for a contact")
    print ("4. Delete a contact")
    print ("5. Exit")

def add_contact(name):
    name = name.title()
    
    if name == '':
        print ("\nInvalid name!\n")
        return
    
    if name in contacts:
        print (f"\nThe contact with name '{name}' is already exist!\n")
        return

    number = input(f"Enter {name}'s number : ")

    if not (number.isdigit()):
        print ("\nEnter a valid number format\n")
        return

    if len(number) != 10:
        print ("\nThe number should be 10 digits\n")
        return
    

    start = []
    start.append(number[0])
    start.append(number[1])
    start.append(number[2])
    
    if start != ['0','5','9'] and start != ['0','5','6']:
        print ("\nThe number introduction format is wrong\nIt should be '059' or '056'\n")
        return
    
    contacts[name] = number

    print (f"\nThe contact with name '{name}' added successfully\n")

def all():
    if not contacts:
        print ("\nThere's no contacts yet\n")
        return
    
    print ("\nAll contacts:")
    for name,number in contacts.items():
        print (f"- {name} : {number}")
    print()

def search():
    if not contacts:
        print ("\nThere's no contacts yet\n")
        return
    
    name = input("Enter the contact name : ")
    
    name = name.title()

    if name == '':
        print ("\nInvalid name!\n")
        return
    
    if name not in contacts:
        print (f"\nThe contact with name '{name}' doesn't exist!\nThe contacts are:")

        for name,number in contacts.items():
            print (f"- {name} : {number}")
        print()
        
        return
    
    print (f"\n{name}'s number is : {contacts[name]}\n")


def delete():
    if not contacts:
        print ("\nThere's no contacts yet\n")
        return
    
    name = input("Enter the contact name : ")
    
    name = name.title()

    if name == '':
        print ("\nInvalid name!\n")
        return
    
    if name not in contacts:
        print (f"\nThe contact with name '{name}' doesn't exist!\nThe contacts are:")

        for name,number in contacts.items():
            print (f"- {name} : {number}")
        print()

        return
    
    del(contacts[name])
    print (f"\nThe contact with name '{name}' deleted successfully\n")


print ("Welcome to Contacts Management System!")
while True:
    menu()
    
    choice = input("Enter your choice here : ")
    if choice == '5':
        break

    elif choice == '1':
        name = input("Enter the contact name : ")
        add_contact(name)

    elif choice == '2':
        all()

    elif choice in ['3','4']:
        if choice == '3': search()
        else: delete()
    
    else:
        print ("\nEnter a Valid option please!\n")

print ("Thank you for using Contacts Management System, Goodbye")

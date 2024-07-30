from datetime import datetime
to_do_list = {}

def display():
    if not to_do_list:
        print ("\nThere's no tasks in the list!\n")
        return
    
    print ("\n The tasks:\n")
    for task , time in to_do_list.items():
        print (f"-{task} on {time} o'clock")

    print()


def add(name , time):
    if name in to_do_list:
        print (f"\nThe task '{name}' is already exist\n")
        return
        
    try:
        task_time = datetime.strptime(f"{time}","%H:%M")
        
    except ValueError:
        print ("\nInvalid time, Please enter a valid time format\n")
        return
    
    for t in to_do_list.values():
        if task_time == t:
            print ("\nYou can't put tow tasks on the same time!\n")
            return
    
    to_do_list[name] = time

    print (f"\nThe task {name} on time {time} added successfully\n")


def remove(name):
    if name not in to_do_list:
        print (f"\nThe task '{name}' doesn't exist!\n")
        return
    
    del to_do_list[name]

    print (f"\nThe task '{name}' removed successfully\n")


print ("Welcome to To-Do-List Management System\n")

while True:
    print ('''Chose an potion
1. Display tasks
2. Add a task
3. Remove a task
4. Exit''')
    
    choice = input("Enter your choice here : ")

    if choice == '4':
        break

    elif choice == '1':
        display()
    
    elif choice == '2' or choice == '3':
        name = input("Enter the task name : ")
        name = name.title()
        
        if not name:
            print ("\nEnter a valid task name!\n")
            continue
        
        if choice == '3':
            remove(name)

        else:
            time = input(f"Enter the {name}'s time (HH:MM) : ")
            add(name , time)

    else:
        print ("\nInvalid input, Please enter a valid option\n")

print ("Thank you for using To-Do-List Management System, Goodbye!")
from statistics import mean

cities = {}
def add_city (name,population):
    if name in cities:
        print ("\nThis city is already exists")
        return
    
    cities[name] = population
    print ("\nThe city has added successfully!")

def update_population(name, population):
    if name not in cities:
        print ("\nThe city doesn't exist")
        return
    
    cities[name] = population
    print (f"\nThe {name}'s population has updated successfully!")

def highest():
    if not cities:
        print ("\nThere's no cities!")
        return
    
    name = ''
    highest = 0
    for city, pop in cities.items():
        if pop > highest:
            highest = pop
            name = city

    print (f"\nThe highest city population it {name} with {highest} people")

def lowest():
    if not cities:
        print ("\nThere's no cities!")
        return
    
    name = ''
    lowest = 1e18
    for city, pop in cities.items():
        if pop < lowest:
            lowest = pop
            name = city

    print (f"\nThe lowest city population it {name} with {lowest} people")

def average():
    if not cities:
        print ("\nThere's no cities!")
        return

    print (f"\nThe average of population for all cities is {mean(cities.values()):.2f}")

print ("Welcome to the Cities Management System!")

while True:
    print ('''\nChoose an option
1. Add a city
2. Update the population of a city
3. Find the city with the highest population
4. Find the city with the lowest population
5. Calculate the average of population for all cities
6. Exit''')

    choice = input("Enter your choice here : ")
    if choice == '6':
        break

    elif choice == '1' or choice == '2':
        name = input("Enter the name of the city : ")
        name = name.title()

        if name == '':
            print ("\nInvalid name")
            continue

        try:
            pop = input(f"Enter the {name}'s population : ")
            pop = int(pop)
            if pop < 0:
                print ("\nEnter a positive number please")
                continue

            if choice == '1':
                add_city(name,pop)

            else:
                update_population(name,pop)

        except ValueError:
            print ("\nEnter a number please")
            continue

    elif choice == '3':
        highest()
    
    elif choice == '4':
        lowest()

    elif choice == '5':
        average()
    
    else:
        print ("\nInvalid input!")

print ("Thank you for using Cities Management System ^_^")

recipes = {}

def add_recipe(recipe_name):
    if recipe_name in recipes:
        print (f"\nThe recipe {recipe_name} is already exists")
        return
    
    recipes[recipe_name] = {}
    print (f"\nThe recipe {recipe_name} has added successfully!")



def add_ingredient(recipe_name, ingredient_name, quantity):
    if recipe_name not in recipes:
        print (f"\nThe recipe {recipe_name} doesn't exist")
        return
    
    recipes[recipe_name][ingredient_name] = quantity
    print (f"\nThe ingredient {ingredient_name} of quantity {quantity} has (added / updated) successfully!")



def remove_recipe(recipe_name):
    if recipe_name not in recipes:
        print (f"\nThe {recipe_name} doesn't exist")
        return
    
    del recipes[recipe_name]
    print (f"\nThe recipe {recipe_name} has removed successfully!")




def get_ingredients(recipe_name):
    if recipe_name not in recipes:
        print (f"\nThe {recipe_name} doesn't exist")
        return
    
    if not recipes[recipe_name]:
        print (f"\nThere's no ingredients for the recipe {recipe_name}")
        return
    
    print (f"\nThe ingredients of {recipe_name} :")
    for ingredient, quantity in recipes[recipe_name].items():
        print (f"{ingredient} : {quantity}")




def all_recipes():
    if not recipes:
        print ("\nThere's no recipes")
        return
    
    print ()
    for recipe in recipes:
        print (f"The ingredients of {recipe} :")
        
        if not recipes[recipe]:
            print (f"There's no ingredients for the recipe {recipe}")
            continue
            
        for ingredient, quantity in recipes[recipe].items():
            print (f"- {ingredient} : {quantity}")

        print ("----------------------------------")


print ("Welcome to the Recipe Management System!")

while True:

    print('''\nChoose an option:
1. Add a recipe
2. Add (or) Update an ingredient
3. remove recipe
4. get recipe's ingredients
5. Display all recipes and those ingredients
6. Exit''')
    
    choice = input("Enter your choice : ")

    if choice == '6':
        break

    elif choice == '1' or choice == '2' or choice == '3' or choice == '4':

        recipe = input("Enter the recipe name : ")
        recipe = recipe.title()

        if not (recipe.isalpha()):
            print ("\nInvalid recipe name!")
            continue

        if choice == '1':
            add_recipe(recipe)

        elif choice == '3':
            remove_recipe(recipe)

        elif choice == '4':
            get_ingredients(recipe)

        else:
            ingredient = input("Enter ingredient name : ")
            ingredient = ingredient.title()

            if not (ingredient.isalpha()):
                print ("\nInvalid ingredient name!")
                continue

            quantity = input(f"Enter the {ingredient}'s quantity : ")

            try:
                quantity = int(quantity)

                if quantity < 0:
                    print ("\nInvalid quantity, enter a positive quantity")
                    continue

                add_ingredient(recipe, ingredient, quantity)

            except ValueError:
                print ("\nInvalid quantity, enter only numbers please")


    elif choice == '5':
        all_recipes()

    else:
        print ("\nInvalid choice!")
        continue

    
print ("Thank you for using Recipe Management System. Good bye!")

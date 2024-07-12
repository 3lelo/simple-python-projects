flag = True
# creating a class named Order contains the order options
class Order:
    # initializing the menu and order
    def __init__(self):

        # the dictionary menu
        self.menu = {"beef" : {"small" : 80, "medium" : 95, "large" : 110},
                     "chicken" : {"small" : 75, "medium" : 90, "large" : 105},
                     "seafood" : {"small" : 110, "medium" : 135, "large" : 150},
                     "pepperoni" : {"small" : 70, "medium" : 90, "large" : 115},}
        
        # the list of order
        self.order = []

    def display_menu(self):
        '''
            displaying the menu for the customers
        '''
        print ("Welcome to our pizza app!\nHere are our pizza options:\n")
        for pizza in self.menu:
            print (f"{pizza} pizza :",end=' ')
            for size in self.menu[pizza].items():
                print (f"{size[0]} for {size[1]} EGP,",end=' ')
            print()
        
    def add_pizza(self,pizza_name,size):
        '''
            add the chosen pizza to the order
        '''

        # check if the chosen pizza is in the menu
        if pizza_name not in self.menu:
            print ("Invalid name")
            return
        
        # check if the size of the chosen pizza is in the menu
        if size not in self.menu[pizza_name]:
            print ("Invalid size")
            return
        
        # add the name and the size and the cost of the pizza to the list of the order
        pizza = [pizza_name,size,self.menu[pizza_name][size]]
        self.order.append(pizza)

    def calculate_total_cost(self):
        '''
            display the information of the order to customer
        '''
        global flag

        # check if the order is empty
        if len(self.order) == 0:
            flag = False
            return
        
        # displaying the information of the order
        cost = 0
        for pizza,size,cst in self.order:
            print (f"- {size} {pizza} pizza")
            cost += cst
        print (f"Total cost: {cost} EGP")
        self.order.clear()

# make an object calls order from the Order class
order = Order()

# call the display_menu method
order.display_menu()


# A while True for take the order from the customer
while True:
    
    # take the name of pizza from customer
    name = input("Enter pizza name or type \"done\" to finish your order : ")
    name = name.lower()

    # if the customer chose to end the order
    if name == 'done':

        # check if the customer chose to end the order and the order stills empty
        if flag == False:
            print ("Your order is empty. Please enter your order.")
            continue

        # call the calculate_total_cost method
        order.calculate_total_cost()

        # ask the customer if he would to order again
        con = input("Would you like to place another order (yes/no): ")
        con = con.lower()

        # end the program if the customer doesn't order again
        if con == 'no':
            print ("Thank you for using our pizza ordering app ^_*")
            break

        continue

    # take the size of the pizza from the customer
    size = input("Enter the size (small, medium, large): ")

    # call the add_pizza method
    order.add_pizza(name,size)

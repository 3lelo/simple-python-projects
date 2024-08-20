class Shoe:
    def __init__(self, model , size , quantity , price):
        self.model = model
        self.size = size
        self.quantity = quantity
        self.price = price

class ShoeInventory:
    def __init__(self):
        self.shoes = []
    
    def add_shoe(self, model , size , quantity , price):
        if not model:
            print ("\nEnter a valid model!\n")
            return
        
        if not (size.isdigit()):
            print ("\nEnter a valid size!\n")
            return
        
        if not (quantity.isdigit()):
            print ("\nEnter a valid quantity!\n")
            return
        
        if not (price.isdigit()):
            print ("\nEnter a valid price!\n")
            return
        
        if quantity < 0 or price < 0:
            print ("\nThe quantity/price should be positive!\n")
            return
        
        if size >= 50 or size <= 10:
            print ("\nThe size should be between 10 and 50\n")
            return

        model = model.upper()
        shoe = Shoe(model , size , quantity , price)
        self.shoes.append(shoe)

        print ("\nThe shoe added successfully\n")

    def check_stock(self, model , size):
        if not model:
            print ("\nEnter a valid model!\n")
            return
        
        if not (size.isdigit()):
            print ("\nEnter a valid size!\n")
            return
        
        model = model.upper()

        for shoe in self.shoes:
            if shoe.model == model and shoe.size == size:
                print (f"\nIn stock : {shoe.quantity} pairs\n")
                return
            
        print ("\nOut of stock!\n")

    def restock_shoe(self, model , size , quantity):
        if not model:
            print ("\nEnter a valid model!\n")
            return
        
        if not (size.isdigit()):
            print ("\nEnter a valid size!\n")
            return
        
        if not (quantity.isdigit()):
            print ("\nEnter a valid quantity!\n")
            return
        
        if quantity <= 0:
            print ("\nEnter a positive quantity!\n")
            return
        
        model = model.upper()

        for shoe in self.shoes:
            if shoe.model == model and shoe.size == size:
                shoe.quantity += quantity
                print (f"\nRestocked {quantity} pairs of {model} (Size {size})\n")
                return
            
        print ("\nOut of stock!\n")

    def sell_shoe(self, model , size , quantity):
        if not model:
            print ("\nEnter a valid model!\n")
            return
        
        if not (size.isdigit()):
            print ("\nEnter a valid size!\n")
            return
        
        if not (quantity.isdigit()):
            print ("\nEnter a valid quantity!\n")
            return
        
        if quantity <= 0:
            print ("\nEnter a positive quantity!\n")
            return
        
        model = model.upper()

        for shoe in self.shoes:
            if shoe.model == model and shoe.size == size:
                if shoe.quantity < quantity:
                    print ("\nQuantity in stock is less than the entered quantity!\n")
                    return
                
                shoe.quantity -= quantity
                print (f"\nSold {quantity} pairs of {model} (Size {size})\n")
                return
        
        print ("\nOut of stock!\n")

    def display_inventory(self):
        if not self.shoes:
            print ("\nInventory is empty!\n")
            return
        
        print ("\nCurrent Inventory:")
        for shoe in self.shoes:
            print (f"{shoe.model} (Size {shoe.size}): {shoe.quantity} pairs, Price per pair: ${shoe.price}")

        print ()

def choices():
    print ("""Shoes Shop Inventory Management
1. Add shoe
2. Check stock
3. Restock shoe
4. Sell shoe
5. Display inventory
6. Exit""")

inventory = ShoeInventory()

while True:
    choices()
    choice = input("Enter your choice (1-6) : ")

    if choice == '6':
        break
    
    elif choice == '1':
        model = input("Enter shoe model : ")
        size = input("Enter shoe size (10-50) : ")
        quantity = input("Enter quantity in stock : ")
        price = input("Enter price per pair : ")
        inventory.add_shoe(model,size,quantity,price)
    
    elif choice == '2':
        model = input("Enter shoe model : ")
        size = input("Enter shoe size : ")
        inventory.check_stock(model,size)

    elif choice in ['3','4']:
        model = input("Enter shoe model : ")
        size = input("Enter shoe size : ")

        if choice == '3':
            quantity = input("Enter quantity to restock (quantity > 0) : ")
            inventory.restock_shoe(model,size,quantity)
        
        else:
            quantity = input("Enter quantity to sell (quantity > 0) : ")
            inventory.sell_shoe(model,size,quantity)

    elif choice == '5':
        inventory.display_inventory()

    else:
        print ("Enter a valid choice!")

print ("Thank you for using Shoes Shop Inventory Management System, Goodbye!")
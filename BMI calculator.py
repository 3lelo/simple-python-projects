def bmi(n,h):
    return round((n / h ** 2) , 2)

print ("Welcome to the BMI Calculator!")
n = input("Enter weight in kilograms (or 'q' to quit): ")
c = 0

while n != 'q' and n != 'Q':

    try:
        n = float(n)
        if n < 0:
            print ("Weight should be positive, try again!")
            n = input("Enter weight in kilograms (or 'q' to quit): ")
            continue
        h = input("Enter height in meters: ")
        try:
            h = float(h)
            if h <= 0:
                print ("Height should be positive, try again!")
                continue

        except ValueError:
            print ("No height entered, try again!")
            continue
        
        c += 1
        b = bmi(n,h)
        print (f"Your BIM is : {b}",end=' --> ')
        if b < 18.5: print ("Underweight")
        elif b <= 24.9: print ("Normal")
        elif b <= 29.9: print ("Overweight")
        elif b <= 34.9: print ("Obese")
        else: print ("Severely Obese")
        n = input("Enter weight in kilograms (or 'q' to quit): ")
    except ValueError:
        print ("No weight entered, try again!")
        n = input("Enter weight in kilograms (or 'q' to quit): ")
        continue

print (f"{c} customers used the program.\nThanks for using the BMI Calculator!")
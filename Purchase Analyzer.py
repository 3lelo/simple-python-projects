from statistics import *
less100 = To499 = To1000 = more1000 = 0
purchase = []
Mean = Median = 0
Mode = []
def purchase_statistics(a):
    global purchase
    global Mean
    global Median
    global Mode
    purchase.append(a)
    Mean = round(mean(purchase),2)
    Median = round(median(purchase),2)
    Mode = multimode(purchase)


print ("Welcome to the Purchase Analyzer!")
amount = input("Enter purchase amount or 'done' for summary statistics: ")


while amount.lower() != 'done':
    try:
        amount = float(amount)
        if amount <= 0:
            print ("Invalid purchase amount, it should be positive.")
            amount = input("Enter purchase amount or 'done' for summary statistics: ")
            continue


        purchase_statistics(amount)
        if amount < 100: less100 += 1
        elif amount <= 499: To499 += 1
        elif amount <= 1000: To1000 += 1
        else: more1000 += 1
        amount = input("Enter purchase amount or 'done' for summary statistics: ")


    except ValueError:
        print ("No purchase data entered. Please enter some purchase amount.")
        amount = input("Enter purchase amount or 'done' for summary statistics: ")


print ("Summary Purchase Statistics:")
print (f"Mean Purchase Amount : {Mean} EGP")
print (f"Median Purchase Amount : {Median} EGP")
print (f"Mode Purchase Amount : {Mode}\n")
print ("Purchase Count by Range:")
print (f"Less than 100 EGP: {less100} purchase")
print (f"100 EGP to 499 EGP: {To499} purchase")
print (f"500 EGP to 1000 EGP: {To1000} purchase")
print (f"More than 1000 EGP: {more1000} purchase")
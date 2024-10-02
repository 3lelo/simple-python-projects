# This is the harvest of five months of training, and there is much more and more.
# Then finally, I got the 5th place in all category (Python Senior)
# 🥈2nd place in best programming (Pytho Senior), at Code Challenge Championship in Egypt

You can run any program you want by removing the comment from it (The programs are between the (=) marks)

```py
# from turtle import *
# Screen()
# bgcolor('skyblue')
# speed(15)
# up()
# goto(0,0)
# down()
# pensize(2)
# fillcolor('green')
# begin_fill()
# bk(2000)
# for _ in range (4):
#     fd(3000)
#     right(90)
# end_fill()
# speed(7)
# up()
# goto(0,0)
# down()
# x = -100
# x_brown = 0
# for _ in range(3):
#     fillcolor('brown')
#     begin_fill()
#     for _ in range(2):
#         fd(20)
#         left(90)
#         fd(60)
#         left(90)
#     end_fill()

#     up()
#     goto(x_brown - 20,60)
#     down()

#     Up = 100
#     for _ in range (3):
#         fillcolor('lightgreen')
#         begin_fill()
#         for _ in range (3):
#             fd(60)
#             left(120)
#         end_fill()
#         up()
#         goto(x_brown - 20,Up)
#         down()
#         Up += 40
#     up()
#     goto(x,0)
#     down()
#     x_brown += -100
#     x += -100
# pencolor('azure4')
# seth(0)
# x_p = 130
# y_p = -80
# for i in range (3):
#     up()
#     goto(x_p,y_p)
#     down()
#     fillcolor('azure4')
#     begin_fill()
#     circle(30)
#     end_fill()


#     up()
#     goto(x_p + 20,y_p - 20)
#     down()
#     fillcolor('azure4')
#     begin_fill()
#     circle(30)
#     end_fill()


#     up()
#     goto(x_p - 20,y_p - 20)
#     down()
#     fillcolor('azure4')
#     begin_fill()
#     circle(30)
#     end_fill()

#     x_p -= 150
#     if i == 0: y_p -= 100
#     elif i == 1: y_p += 80
# up()
# goto(0,0)
# pencolor('black')
# fd(100)
# down()
# left(90)
# fd(60)
# bk(30)
# right(90)
# fd(200)
# left(90)
# fd(30)
# bk(60)
# ht()
# exitonclick()




# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================




# class Student:
#     def __init__(self, name,age,grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
    
# class Course:
#     def __init__(self, name,max):
#         self.name = name
#         self.max = max
#         self.students = []
    
#     def add_student(self, student):
#         if len(self.students) < self.max:
#             self.students.append(student)
#             return True
#         else:
#             return False
        
#     def get_avr_grade(self):
#         sum = 0
#         for student in self.students:
#             sum += student.grade
#         return sum / len(self.students)
    
# s1 = Student("Ali", 16, 95)
# s2 = Student("Mohamed", 17, 85)
# s3 = Student("Ahmad", 19, 75)
# s4 = Student("Khaled", 14, 90)

# course = Course ("Math", 3)
# course.add_student(s1)
# course.add_student(s2)
# course.add_student(s3)
# cnt = 1
# for i in course.students:
#     print (f"the student number {cnt}\n")
#     print (f"Name : {i.name}\nAge : {i.age}\nGrade : {i.grade}\n--------------------")
#     cnt += 1

# print (f"The average of the grades in course {course.get_avr_grade()}")
# print (f"Can i add another student? '{course.add_student(s4)}'")




# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================




# 1
# for _ in range (10): print('* ',end='')

# 2
# for _ in range (5): print('* ' * 5)

# 3
# for i in range (1,6): print ('* ' * i)

# 4
# for i in range (5,0,-1): print ('* ' * i)

# 5
# for i in range (1,6): print ((' ' * (5-i)) + ('* ' * i))
# for i in range (4,0,-1): print ((' ' * (5-i)) + ('* ' * i))

# Assignment
# n = int(input("Enter the height : "))
# for i in range (int(input("Enter the width : "))): print ('*' * n)




# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================




# from time import *
# print (strftime('%A')) # اسم اليوم بالكامل
# print (strftime('%a')) #اختصار اسم اليوم
# print (strftime('%w')) # رقم اليوم في الأسبوع
# print (strftime('%d')) # رقم اليوم في الشهر مسبوق بـ0
# print (strftime('%d').lstrip('0'),'\n') # رقم اليوم في الشهر بدون 0
# print (strftime('%b')) # اختصار اسم الشهر
# print (strftime('%B')) # اسم الشهر بالكامل
# print (strftime('%m')) # رقم الشهر مسبوق بـ0
# print (strftime('%m').lstrip('0'),'\n') # رثم الشهر بدون 0
# print (strftime('%Y'),'\n') # السنة
# print (strftime('%H')) # الساعة بنظام الـ24 مسبوق بـ0
# print (strftime('%H').lstrip('0')) # الساعة بنظام الـ24 بدون 0
# print (strftime('%I')) # الساعة بنظام الـ12 مسبوق بـ0
# print (strftime('%I').lstrip('0'),'\n') # الساعة بنظام الـ12 بدون صفر
# print (strftime('%p'),'\n') # AM OR PM
# print (strftime('%M')) # الدقيقة مسبوق بـ0
# print (strftime('%M').lstrip('0'),'\n') # الدقيقة بدون 0
# print (strftime('%S')) # الثانية مسبوق بـ0
# print (strftime('%S').lstrip('0'),'\n') # الثانية بدون 0
# print (strftime('%j')) # اليوم بالنسبة للسنة مسبوق بـ0
# print (strftime('%j').lstrip('0'),'\n') # اليوم بالنسبة للسنة بدون 0
# print (strftime('%U')) # الأسبوع بالنسبة للسنة مسبوق بـ0




# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================




# def bmi(n,h):
#     return round((n / h ** 2) , 2)

# print ("Welcome to the BMI Calculator!")
# n = input("Enter weight in kilograms (or 'q' to quit): ")
# c = 0
# n = n.lower()

# while n != 'q':

#     try:
#         n = float(n)
#         if n < 0:
#             print ("Weight should be positive, try again!")
#             n = input("Enter weight in kilograms (or 'q' to quit): ")
#             continue
#         h = input("Enter height in meters: ")
#         try:
#             h = float(h)
#             if h <= 0:
#                 print ("Height should be positive, try again!")
#                 continue

#         except ValueError:
#             print ("No height entered, try again!")
#             continue
        
#         c += 1
#         b = bmi(n,h)
#         print (f"Your BIM is : {b}",end=' --> ')
#         if b < 18.5: print ("Underweight")
#         elif b <= 24.9: print ("Normal")
#         elif b <= 29.9: print ("Overweight")
#         elif b <= 34.9: print ("Obese")
#         else: print ("Severely Obese")
#         n = input("Enter weight in kilograms (or 'q' to quit): ")
#     except ValueError:
#         print ("No weight entered, try again!")
#         n = input("Enter weight in kilograms (or 'q' to quit): ")
#         continue

# print (f"{c} customers used the program.\nThanks for using the BMI Calculator!")




# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================




# from statistics import mean,median,multimode
# less100 = To499 = To1000 = more1000 = 0
# purchase = []
# Mean = Median = 0
# Mode = []
# def purchase_statistics(a):
#     global purchase
#     global Mean
#     global Median
#     global Mode
#     purchase.append(a)
#     Mean = round(mean(purchase),2)
#     Median = round(median(purchase),2)
#     Mode = multimode(purchase)


# print ("Welcome to the Purchase Analyzer!")
# amount = input("Enter purchase amount or 'done' for summary statistics: ")


# while amount.lower() != 'done':
#     try:
#         amount = float(amount)
#         if amount <= 0:
#             print ("Invalid purchase amount, it should be positive.")
#             amount = input("Enter purchase amount or 'done' for summary statistics: ")
#             continue


#         purchase_statistics(amount)
#         if amount < 100: less100 += 1
#         elif amount <= 499: To499 += 1
#         elif amount <= 1000: To1000 += 1
#         else: more1000 += 1
#         amount = input("Enter purchase amount or 'done' for summary statistics: ")


#     except ValueError:
#         print ("No purchase data entered. Please enter some purchase amount.")
#         amount = input("Enter purchase amount or 'done' for summary statistics: ")


# print ("Summary Purchase Statistics:")
# print (f"Mean Purchase Amount : {Mean} EGP")
# print (f"Median Purchase Amount : {Median} EGP")
# print (f"Mode Purchase Amount : {Mode}\n")
# print ("Purchase Count by Range:")
# print (f"Less than 100 EGP: {less100} purchase")
# print (f"100 EGP to 499 EGP: {To499} purchase")
# print (f"500 EGP to 1000 EGP: {To1000} purchase")
# print (f"More than 1000 EGP: {more1000} purchase")




# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================




# class Book:
#     def __init__(self, title,author,publication_year):
#         self.title = title
#         self.author = author
#         self.publication_year = publication_year
#     def __repr__(self):
#         return f"{self.title} by {self.author} on {self.publication_year}"
    
# class Library:
#     def __init__(self):
#         self.books = []
#     def add_book(self,book):
#         self.books.append(book)
#     def remove_book(self,book_title):
#         flag = False
#         for book in self.books:
#             if book.title == book_title:
#                 flag = True
#                 break
#         if not flag:
#             print ("Invalid!")
#             return
#         self.books = [b for b in self.books if b.title != book_title]
#     def find_books_by_author(self,author):
#         return [b for b in self.books if b.author == author]
#     def list_books(self):
#         return [str(b) for b in self.books]
    
# book1 = Book("Jaloudi is 'GAY'","3mk Ali",2024)
# book2 = Book("Islam is 'GAY'","3mk Ali",2024)
# book3 = Book("No one's 'GAY'","Ameer",2025)
# x = Library()
# x.add_book(book1)
# x.add_book(book2)
# x.add_book(book3)
# for i in x.list_books():
#     print (i)
# x.remove_book("Hi")
# x.remove_book("No one's 'GAY'")
# for i in x.list_books():
#     print (i)
# x.add_book(book3)
# print (x.find_books_by_author("3mk Ali"))
# for i in x.list_books():
#     print (i)




# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================




# from statistics import *
# class Student:
#     def __init__(self,name,age,grades:list):
#         self.name = name
#         self.age = age
#         self.grades = grades

#     def add_grade(self,grade):
#         self.grades.append(grade)

#     def average_grade(self):
#         return mean(self.grades)
    
#     def __repr__(self):
#         return f'name : {self.name}, age : {self.age}, grades : {self.grades}'
    
# class Classroom:
#     def __init__(self,students:list):
#         self.students = students

#     def add_student(self,student):
#         self.students.append(student)

#     def remove_student(self,student_name):
#         found = False
#         for i in self.students:
#             if i.name == student_name:
#                 found = True
#                 break
#         if not found:
#             print ("Student not found!")
#             return
#         self.students = [i for i in self.students if i.name != student_name]

#     def get_student_average(self,student_name):
#         for i in self.students:
#             if i.name == student_name:
#                 return i.average_grade()
#         return None
            
#     def class_average(self):
#         if len(self.students) == 0: return None
#         avr = []
#         for i in self.students:
#             avr.append(i.average_grade())
#         return mean(avr)
    
#     def __repr__(self):
#         return f'{self.students}'

# x = Student("Ali", 15, [10, 9, 8, 9, 10])
# y = Student("Mohammad", 15, [10, 9, 4, 8, 0])
# z = Student("Ali", 15, [10, 9, 8, 8, 7])
# a = Student("Yousef", 15, [10, 9, 8, 9, 8])

# ans = Classroom([x, y, z])
# ans.add_student(a)

# print(ans)
# print(f"Class average: {ans.class_average()}")

# print(f"Average of Mohammad: {ans.get_student_average('Mohammad')}")

# ans.remove_student("Ali")
# print(ans)
# print(f"Class average after removing Ali: {ans.class_average()}")

# ans.remove_student("Ali")
# print(ans.get_student_average("Ali"))
# print(ans.get_student_average("Mohammad"))
# ans.remove_student("Mohammad")
# ans.remove_student("Yousef")
# print (ans.class_average())




# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================




# import turtle
# from random import randint

# sc = turtle.Screen()
# sc.setup(500, 500)
# turtle.colormode(255)
# pen = turtle.Turtle()
# x = 0
# y = -50
# pen.speed(20)
# pen.penup()
# pen.goto(x, y)
# pen.pendown()
# def draw_star(num, angle):
#     k = 100
#     for _ in range(num):
#         a = randint(0, 255)
#         b = randint(0, 255)
#         c = randint(0, 255)
#         pen.fillcolor(a, b, c)
#         pen.color(a, b, c)
#         pen.begin_fill()
        
#         for _ in range(5):
#             pen.forward(k)
#             pen.right(angle)
#             pen.forward(k)
#             pen.right(72 - angle)
#         k -= (k // num)
#         global y
#         y += 10
#         pen.end_fill()
#         pen.penup()
#         pen.goto(x, y)
#         pen.pendown()
        
# numberOfStars = 20
# starAngle = 144

# draw_star(numberOfStars, starAngle)

# turtle.done()




# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================




# import turtle
# from random import randint

# sc = turtle.Screen()
# sc.setup(800, 800)
# sc.bgcolor("black")
# pen = turtle.Turtle()
# pen.seth(90)
# pen.speed(0)

# def star():
#     pen.pencolor('white')
#     for _ in range(5):
#         pen.forward(5)
#         pen.right(150)
#         pen.forward(5)
#         pen.right(-78)

# def moon():
#     pen.speed(5)
#     pen.penup()
#     pen.goto(100, 250)
#     pen.pendown()
#     pen.fillcolor('white')
#     pen.begin_fill()
#     pen.circle(100)
#     pen.end_fill()

# def full_pic(num):
#     for _ in range(num):
#         pen.penup()
#         x = randint(-800, 500)
#         y = randint(-800, 500)
#         pen.goto(x, y)
#         pen.pendown()
#         star()

#     moon()        

# number_of_stars = 100
# full_pic(number_of_stars)
# pen.hideturtle()
# sc.exitonclick()




# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================




# play = input("if you want to play enter 'yes' or enter 'no' : ").lower()
# while play != 'no':
#     xo = [['.','.','.'],['.','.','.'],['.','.','.']]
#     flag = False
#     for q in range (1,10):
#         if q % 2 == 1: print ("X turn\n=====================")
#         else: print ("O turn\n=====================")
#         x, y = map(int,input("Enter the column and row (1 - 3) : ").split())
#         x -= 1
#         y -= 1
#         if q % 2 == 1: xo[x][y] = 'X'
#         else: xo[x][y] = 'O'
#         print()
#         for i in range(3):
#             for j in range (3):
#                 print (xo[i][j],end=' ')
#             print()
#         print()

#         if ((xo[0][0] == xo[1][0] == xo[2][0] and xo[0][0] != '.')
#             or (xo[0][0] == xo[0][1] == xo[0][2] and xo[0][0] != '.')
#             or (xo[0][0] == xo[1][1] == xo[2][2] and xo[1][1] != '.')
#             or (xo[0][2] == xo[1][1] == xo[2][0] and xo[1][1] != '.')
#             or (xo[1][0] == xo[1][1] == xo[1][2] and xo[1][1] != '.')
#             or (xo[2][0] == xo[2][1] == xo[2][2] and xo[2][2] != '.')
#             or (xo[0][1] == xo[1][1] == xo[2][1] and xo[1][1] != '.')
#             or (xo[0][2] == xo[1][2] == xo[2][2] and xo[2][2] != '.')):
#             flag = True
#             if q % 2 == 1: print ("The winner is 'X'")
#             else: print ("The winner is 'Y'")
#             break
#     if not flag: print ("Draw!")
#     play = input("if you want to play again enter 'yes' or enter 'no' : ").lower()




# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================




# import turtle
# sc = turtle.Screen()
# pen = turtle.Turtle()
# def square(size,color):
#     pen.fillcolor(color)
#     side = 0
#     if size == 3: side = 200
#     elif size == 2: side = 100
#     else: side = 50
#     pen.begin_fill()
#     for i in range(4):
#         pen.forward(side)
#         pen.left(90)
#     pen.end_fill()

# def triangle(size,color):
#     pen.fillcolor(color)
#     side = 0
#     if size == 3: side = 200
#     elif size == 2: side = 100
#     else: side = 50
#     pen.begin_fill()
#     for i in range(3):
#         pen.forward(side)
#         pen.left(120)
#     pen.end_fill()

# def rectangle(size,color):
#     pen.fillcolor(color)
#     side = 0
#     if size == 3: side = 200
#     elif size == 2: side = 100
#     else: side = 50
#     pen.begin_fill()
#     for i in range(2):
#         pen.forward(side)
#         pen.left(90)
#         pen.forward(side // 2)
#         pen.left(90)
#     pen.end_fill()

# def Circle(size,color):
#     side = 0
#     if size == 3: side = 200
#     elif size == 2: side = 100
#     else: side = 50
#     pen.fillcolor(color)
#     pen.begin_fill()
#     pen.circle(side)
#     pen.end_fill()
# print('Welcome To the "Shapes For Fun" Interactive Game!')
# shape=input('Enter the shape (square, triangle, rectangle, circle): ')
# size=int(input('Enter the size (1 for small, 2 for medium, 3 for large): '))
# color=input('Enter the color (red, green, blue, orange, yellow): ')
# if shape.lower()=='square':
#   square(size,color)
# elif shape.lower()=='rectangle':
#   rectangle(size,color)
# elif shape.lower()=='triangle':
#   triangle(size,color)
# elif shape.lower()=='circle':
#   Circle(size,color)
# sc.exitonclick()




# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================




# import turtle
# from random import randint
# def circle(size,num):
#     for i in range(num):
#         r = randint(0,255)
#         g = randint(0,255)
#         b = randint(0,255)
#         pen.color(r,g,b)
#         pen.circle(size)
#         pen.left((360 / num))

# def draw():
#     number = input("Enter the number of circles or 'quit' to exit : ")
#     while number.lower() != 'quit':
#         try:
#             num = int(number)
#             match num:
#                 case x if x <= 0:
#                     print ("Enter a positive number")
#                     number = input("Enter the number of circles or 'quit' to exit : ")
#                     continue
#             try:
#                 size = input("Enter the size for each circle : ")
#                 size = int(size)
#                 match size:
#                     case x if x <= 0:
#                         print ("Enter a positive number")
#                         continue
#                 circle(size,num)
#                 break
#             except ValueError:
#                 print ("Enter an int please")
#         except ValueError:
#             print ("Enter an int please")
#             number = input("Enter the number of circles or 'quit' to exit : ")

# sc = turtle.Screen()
# sc.bgcolor("black")
# sc.colormode(255)
# sc.setup(650,650)
# pen = turtle.Turtle()
# pen.speed(0)
# pen.pensize(2)
# pen.up()
# pen.goto(0,0)
# pen.down()
# pen.hideturtle()
# draw()

# sc.exitonclick()




# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================




# # creating a class named Order contains the order options
# class Order:
#     # initializing the menu and order
#     def __init__(self):

#         # the dictionary menu
#         self.menu = {"beef" : {"small" : 80, "medium" : 95, "large" : 110},
#                      "chicken" : {"small" : 75, "medium" : 90, "large" : 105},
#                      "seafood" : {"small" : 110, "medium" : 135, "large" : 150},
#                      "pepperoni" : {"small" : 70, "medium" : 90, "large" : 115},}
        
#         # the list of order
#         self.order = []

#     def display_menu(self):
#         '''
#             displaying the menu for the customers
#         '''
#         print ("Welcome to our pizza app!\nHere are our pizza options:\n")
#         for pizza in self.menu:
#             print (f"{pizza} pizza :",end=' ')
#             for size in self.menu[pizza].items():
#                 print (f"{size[0]} for {size[1]} EGP,",end=' ')
#             print()
        
#     def add_pizza(self,pizza_name,size):
#         '''
#             add the chosen pizza to the order
#         '''

#         # check if the chosen pizza is in the menu
#         if pizza_name not in self.menu:
#             print ("Invalid name")
#             return
        
#         # check if the size of the chosen pizza is in the menu
#         if size not in self.menu[pizza_name]:
#             print ("Invalid size")
#             return
        
#         # add the name and the size and the cost of the pizza to the list of the order
#         pizza = [pizza_name,size,self.menu[pizza_name][size]]
#         self.order.append(pizza)

#     def check_empty_order(self) -> bool:

#         # check if the order is empty
#         if len(self.order) == 0: return False
#         return True

#     def calculate_total_cost(self):
#         '''
#             display the information of the order to customer
#         '''

#         # displaying the information of the order
#         cost = 0
#         for pizza,size,cst in self.order:
#             print (f"- {size} {pizza} pizza")
#             cost += cst
#         print (f"Total cost: {cost} EGP")
#         self.order.clear()

# # make an object calls order from the Order class
# order = Order()

# # call the display_menu method
# order.display_menu()


# # A while True for take the order from the customer
# while True:
    
#     # take the name of pizza from customer
#     name = input("Enter pizza name or type \"done\" to finish your order : ")
#     name = name.lower()

#     # if the customer chose to end the order
#     if name == 'done':

#         # call the check_empty_order method
#         empty = order.check_empty_order()

#         # check if the customer chose to end the order and the order stills empty
#         if empty == False:
#             print ("Your order is empty. Please enter your order.")
#             continue

#         # call the calculate_total_cost method
#         order.calculate_total_cost()

#         # ask the customer if he would to order again
#         con = input("Would you like to place another order (yes/no): ")
#         con = con.lower()

#         # end the program if the customer doesn't order again
#         if con == 'no':
#             print ("Thank you for using our pizza ordering app ^_*")
#             break

#         continue

#     # take the size of the pizza from the customer
#     size = input("Enter the size (small, medium, large): ")

#     # call the add_pizza method
#     order.add_pizza(name,size)




# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================




# from datetime import datetime
# to_do_list = {}

# def display():
#     if not to_do_list:
#         print ("\nThere's no tasks in the list!\n")
#         return
    
#     print ("\n The tasks:\n")
#     for task , time in to_do_list.items():
#         print (f"-{task} on {time} o'clock")

#     print()


# def add(name , time):
#     if name in to_do_list:
#         print (f"\nThe task '{name}' is already exist\n")
#         return
        
#     try:
#         task_time = datetime.strptime(f"{time}","%H:%M")
        
#     except ValueError:
#         print ("\nInvalid time, Please enter a valid time format\n")
#         return
    
#     for t in to_do_list.values():
#         if task_time == t:
#             print ("\nYou can't put tow tasks on the same time!\n")
#             return
    
#     to_do_list[name] = time

#     print (f"\nThe task {name} on time {time} added successfully\n")


# def remove(name):
#     if name not in to_do_list:
#         print (f"\nThe task '{name}' doesn't exist!\n")
#         return
    
#     del to_do_list[name]

#     print (f"\nThe task '{name}' removed successfully\n")

# print ("Welcome to To-Do-List Management System\n")
# while True:
#     print ('''Chose an potion
# 1. Display tasks
# 2. Add a task
# 3. Remove a task
# 4. Exit''')
    
#     choice = input("Enter your choice here : ")

#     if choice == '4':
#         break

#     elif choice == '1':
#         display()
    
#     elif choice in ['2','3']:
#         name = input("Enter the task name : ")
#         name = name.title()

#         if not name:
#             print ("\nEnter a valid task name!\n")
#             continue
        
#         if choice == '3':
#             remove(name)

#         else:
#             time = input(f"Enter the {name}'s time (HH:MM) : ")
#             add(name , time)

#     else:
#         print ("\nInvalid input, Please enter a valid option\n")

# print ("Thank you for using To-Do-List Management System, Goodbye!")




# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================




# contacts = {}
# def menu():
#     print ("Enter an option:")
#     print ("1. Add a contact")
#     print ("2. View all contacts")
#     print ("3. Search for a contact")
#     print ("4. Delete a contact")
#     print ("5. Exit")

# def add_contact(name):
#     name = name.title()
    
#     if name == '':
#         print ("\nInvalid name!\n")
#         return
    
#     if name in contacts:
#         print (f"\nThe contact with name '{name}' is already exist!\n")
#         return

#     number = input(f"Enter {name}'s number : ")

#     if not (number.isdigit()):
#         print ("\nEnter a valid number format\n")
#         return

#     if len(number) != 10:
#         print ("\nThe number should be 10 digits\n")
#         return
    

#     start = []
#     start.append(number[0])
#     start.append(number[1])
#     start.append(number[2])
    
#     if start != ['0','5','9'] and start != ['0','5','6']:
#         print ("\nThe number introduction format is wrong\nIt should be '059' or '056'\n")
#         return
    
#     contacts[name] = number

#     print (f"\nThe contact with name '{name}' added successfully\n")

# def all():
#     if not contacts:
#         print ("\nThere's no contacts yet\n")
#         return
    
#     print ("\nAll contacts:")
#     for name,number in contacts.items():
#         print (f"- {name} : {number}")
#     print()

# def search():
#     if not contacts:
#         print ("\nThere's no contacts yet\n")
#         return
    
#     name = input("Enter the contact name : ")
    
#     name = name.title()

#     if name == '':
#         print ("\nInvalid name!\n")
#         return
    
#     if name not in contacts:
#         print (f"\nThe contact with name '{name}' doesn't exist!\nThe contacts are:")

#         for name,number in contacts.items():
#             print (f"- {name} : {number}")
#         print()
        
#         return
    
#     print (f"\n{name}'s number is : {contacts[name]}\n")


# def delete():
#     if not contacts:
#         print ("\nThere's no contacts yet\n")
#         return
    
#     name = input("Enter the contact name : ")
    
#     name = name.title()

#     if name == '':
#         print ("\nInvalid name!\n")
#         return
    
#     if name not in contacts:
#         print (f"\nThe contact with name '{name}' doesn't exist!\nThe contacts are:")

#         for name,number in contacts.items():
#             print (f"- {name} : {number}")
#         print()

#         return
    
#     del(contacts[name])
#     print (f"\nThe contact with name '{name}' deleted successfully\n")


# print ("Welcome to Contacts Management System!")
# while True:
#     menu()
    
#     choice = input("Enter your choice here : ")
#     if choice == '5':
#         break

#     elif choice == '1':
#         name = input("Enter the contact name : ")
#         add_contact(name)

#     elif choice == '2':
#         all()

#     elif choice in ['3','4']:
#         if choice == '3': search()
#         else: delete()
    
#     else:
#         print ("\nEnter a Valid option please!\n")

# print ("Thank you for using Contacts Management System, Goodbye")




# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================




# from random import choice

# print("Welcome to Hangman Game!")
# fruits = ["lemon", "kiwi", "apple", "orange", "pineapple", "banana", "strawberry","mango","watermelon"]

# def word():
#     global fruits

#     fruit = choice(fruits)
#     n = len(fruit)

#     win = tries = 0

#     print(f"\nGuess the fruit:\nYou have {n} tries to guess")

#     empty = ["_ "] * n

#     print("".join(empty))

#     s = set(fruit)

#     while tries <= n:
#         if win == len(s):
#             fruits = [f for f in fruits if f != fruit]
#             print("\nYou won :)\n")
#             return
        
#         guess = input("Enter a letter to guess: ")
#         guess = guess.lower()

#         if not guess.isalpha() or len(guess) > 1:
#             print("\nPlease enter one letter\n")
#             continue
        
#         if guess in fruit:
#             for g in range(n):
#                 if fruit[g] == guess:
#                     empty[g] = guess + ' '
#             win += 1
        
#         else:
#             print("\nYou guessed wrong :(")

#         print("".join(empty))

#         tries += 1

#     print("\nYou lose :(\n")

# word()

# while fruits:
#     again = input("You want to play again? (yes/no) : ")
#     again = again.lower()

#     if again == 'no':
#         break

#     elif again == 'yes':
#         word()

#     else:
#         print ("\nPlease enter a valid input\n")

# print ("Thank you for playing, Goodbye")




# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================




# class Shoe:
#     def __init__(self, model , size , quantity , price):
#         self.model = model
#         self.size = size
#         self.quantity = quantity
#         self.price = price

# class ShoeInventory:
#     def __init__(self):
#         self.shoes = []
    
#     def add_shoe(self, model , size , quantity , price):
#         if not model:
#             print ("\nEnter a valid model!\n")
#             return
        
#         if not (size.isdigit()):
#             print ("\nEnter a valid size!\n")
#             return
#         size = int(size)
        
#         if not (quantity.isdigit()):
#             print ("\nEnter a valid quantity!\n")
#             return
        
#         quantity = int(quantity)
        
#         if not (price.isdigit()):
#             print ("\nEnter a valid price!\n")
#             return
        
#         price = int(price)
        
#         if quantity < 0 or price < 0:
#             print ("\nThe quantity/price should be positive!\n")
#             return
        
#         if size > 50 or size < 10:
#             print ("\nThe size should be between 10 and 50\n")
#             return

#         model = model.upper()
#         shoe = Shoe(model , size , quantity , price)
#         self.shoes.append(shoe)

#         print ("\nThe shoe added successfully\n")

#     def check_stock(self, model , size):
#         if not model:
#             print ("\nEnter a valid model!\n")
#             return
        
#         if not (size.isdigit()):
#             print ("\nEnter a valid size!\n")
#             return
        
#         size = int(size)
#         model = model.upper()

#         for shoe in self.shoes:
#             if shoe.model == model and shoe.size == size:
#                 print (f"\nIn stock : {shoe.quantity} pairs\n")
#                 return
            
#         print ("\nOut of stock!\n")

#     def restock_shoe(self, model , size , quantity):
#         if not model:
#             print ("\nEnter a valid model!\n")
#             return
        
#         if not (size.isdigit()):
#             print ("\nEnter a valid size!\n")
#             return
        
#         size = int(size)
        
#         if not (quantity.isdigit()):
#             print ("\nEnter a valid quantity!\n")
#             return
        
#         quantity = int(quantity)
        
#         if quantity <= 0:
#             print ("\nEnter a positive quantity!\n")
#             return
        
#         model = model.upper()

#         for shoe in self.shoes:
#             if shoe.model == model and shoe.size == size:
#                 shoe.quantity += quantity
#                 print (f"\nRestocked {quantity} pairs of {model} (Size {size})\n")
#                 return
            
#         print ("\nOut of stock!\n")

#     def sell_shoe(self, model , size , quantity):
#         if not model:
#             print ("\nEnter a valid model!\n")
#             return
        
#         if not (size.isdigit()):
#             print ("\nEnter a valid size!\n")
#             return
        
#         size = int(size)
        
#         if not (quantity.isdigit()):
#             print ("\nEnter a valid quantity!\n")
#             return
        
#         quantity = int(quantity)
        
#         if quantity <= 0:
#             print ("\nEnter a positive quantity!\n")
#             return
        
#         model = model.upper()

#         for shoe in self.shoes:
#             if shoe.model == model and shoe.size == size:
#                 if shoe.quantity < quantity:
#                     print ("\nQuantity in stock is less than the entered quantity!\n")
#                     return
                
#                 shoe.quantity -= quantity
#                 print (f"\nSold {quantity} pairs of {model} (Size {size})\n")
#                 return
        
#         print ("\nOut of stock!\n")

#     def display_inventory(self):
#         if not self.shoes:
#             print ("\nInventory is empty!\n")
#             return
        
#         print ("\nCurrent Inventory:")
#         for shoe in self.shoes:
#             print (f"{shoe.model} (Size {shoe.size}): {shoe.quantity} pairs, Price per pair: ${shoe.price}")

#         print ()

# def choices():
#     print ("""Shoes Shop Inventory Management
# 1. Add shoe
# 2. Check stock
# 3. Restock shoe
# 4. Sell shoe
# 5. Display inventory
# 6. Exit""")

# inventory = ShoeInventory()

# while True:
#     choices()
#     choice = input("Enter your choice (1-6) : ")

#     match choice:
#         case '6':
#             break
    
#         case '1':
#             model = input("Enter shoe model : ")
#             size = input("Enter shoe size (10-50) : ")
#             quantity = input("Enter quantity in stock : ")
#             price = input("Enter price per pair : ")
#             inventory.add_shoe(model,size,quantity,price)
    
#         case'2':
#             model = input("Enter shoe model : ")
#             size = input("Enter shoe size : ")
#             inventory.check_stock(model,size)

#         case choice if choice in ['3','4']:
#             model = input("Enter shoe model : ")
#             size = input("Enter shoe size : ")

#             match choice:
#                 case '3':
#                     quantity = input("Enter quantity to restock (quantity > 0) : ")
#                     inventory.restock_shoe(model,size,quantity)
                
#                 case _:
#                     quantity = input("Enter quantity to sell (quantity > 0) : ")
#                     inventory.sell_shoe(model,size,quantity)

#         case '5':
#             inventory.display_inventory()

#         case _:
#             print ("Enter a valid choice!")

# print ("Thank you for using Shoes Shop Inventory Management System, Goodbye!")




# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================




# from math import pi

# def choices():
#     print ("""Enter a shape number to calculate its area
# 1. circle
# 2. square
# 3. rectangle
# 4. triangle
# 5. exit""")
    
# def square(side):
#     if int(side) <= 0:
#         print ("Enter a positive number please")
#         return

#     if not (side.isdigit()):
#         print ("\nEnter an int number please\n")
#         return
    
#     side = int(side)

#     area = side **2
#     print (f"\nThe area is : {area:.2f}\n")

# def circle(radius):
#     if int(radius) <= 0:
#         print ("Enter a positive number please")
#         return

#     if not (radius.isdigit()):
#         print ("\nEnter an int number please\n")
#         return
    
#     radius = int(radius)

#     area = pi * (radius ** 2)
#     print (f"\nThe area is : {area:.2f}\n")

# def rectangle(length,width):
#     if int(length) <= 0 or int(width) <= 0:
#         print ("Enter a positive number please")
#         return

#     if not (length.isdigit()) or not (width.isdigit()):
#         print ("\nEnter an int numbers please\n")
#         return
    
#     length = int(length)
#     width = int(width)

#     area = length * width
#     print (f"\nThe area is : {area:.2f}\n")

# def triangle(height,base):
#     if int(height) <= 0 or int(base) <= 0:
#         print ("Enter a positive number please")
#         return

#     if not (height.isdigit()) or not (base.isdigit()):
#         print ("\nEnter an int numbers please")
#         return
    
#     height = int(height)
#     base = int(base)

#     area = (height * base) / 2
#     print (f"\nThe area is : {area:.2f} \n")

# while True:
#     choices()
#     choice = input("Enter your choice (1 - 5) : ")

#     if choice == '5':
#         break
    
#     elif choice == '1':
#         r = input("Enter the radius : ")
#         circle(r)

#     elif choice == '2':
#         side = input("Enter the side : ")
#         square(side)

#     elif choice == '3':
#         l = input("Enter the length : ")
#         w = input("Enter the width : ")
#         rectangle(l,w)

#     elif choice == '4':
#         h = input("Enter the height : ")
#         b = input("Enter the base : ")
#         triangle(h,b)

#     else:
#         print ("\nEnter a valid choice!\n")




# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================




# # BookInventory management


# def menu():
#     '''A function to display the options for user'''
#     print ("Options :")
#     print ("1. Add book")
#     print ("2. Check stock")
#     print ("3. Sell book")
#     print ("4. Restock book")
#     print ("5. Display Inventory")
#     print ("6. Exit")



# def check(input : str,type : str)-> bool:
#     '''A function to check if the user ignoring to input something'''
#     if not input:
#         print (f"The {type} shouldn't be empty!\n")
#         return False
#     return True



# def ISBN(isbn : str) -> bool:
#     '''A function to check if the ISBN length is equal to 10 or not'''
#     if len(isbn) != 10:
#         print ("ISBN length should be 10!\n")
#         return False
#     return True



# def Quantity(q : str) -> bool:
#     '''A function to check for the quantity if it not an integer or less than 1'''
#     if not (q.isdigit()) or int(quantity) < 1:
#         print ("Quantity should be at least 1!\n")
#         return False
#     return True




# class Book:
#     '''Class for the book'''
#     def __init__ (self,title,author,isbn,quantity,price):
#         '''Initialize the book characteristics'''
#         self.title = title
#         self.author = author
#         self.isbn = isbn
#         self.quantity = quantity
#         self.price = price



# class ShopInventory:
#     '''Class for the Shop Inventory'''
#     def __init__(self):
#         '''Initialize the Shop Inventory by make an empty list'''
#         self.books = []
    
#     def FindBookByIsbn(self,isbn : str) -> Book:
#         '''A helper method to find a book by ISBN'''
#         for book in self.books:
#             if book.isbn == isbn:
#                 return book
        
#         return None


#     def add(self,title : str,author : str,isbn : str,quantity : int,price : int)-> None:
#         '''A method to make an object of the book class and check if the ISBN isn't already
#         exists and add it to the inventory'''
#         book = Book(title,author,isbn,quantity,price)
        
#         if self.FindBookByIsbn(isbn):
#             print ("The ISBN is already exists!\n")
#             return
        
#         self.books.append(book)
#         print (f"Added book : {title} by {author}\n")




#     def sell(self,isbn : str, quantity : int) -> None:
#         '''A method to sell a book from the inventory'''
#         book = self.FindBookByIsbn(isbn)

#         if book:
#             # Send a message to the user if the book quantity is less than the sell quantity
#             if book.quantity < quantity:
#                 print (f"There's just {book.quantity} copies of {book.title}!\n")
#                 return
            
#             book.quantity -= quantity
#             print (f"Sold {quantity} copies of {book.title}\n")

#         else:
#             # Send a message to the user if the book isn't in the inventory
#             print ("Book not found!\n")



#     def check(self,isbn : str) -> None:
#         '''A method to check the book stock in inventory and display it'''
#         book = self.FindBookByIsbn(isbn)
        
#         if book:
#             print (f"Title : {book.title}, Stock : {book.quantity} copies\n")

#         else:
#             # Send a message to the user if the book is out of stock
#             print ("Book not found!\n")




#     def restock(self,isbn : str,quantity : str) -> None:
#         '''A method to restock the book and display the new stock'''
#         book = self.FindBookByIsbn(isbn)
        
#         if book:
#             book.quantity += quantity
#             print (f"Restocked {quantity} copies of {book.title}, New stock : {book.quantity}\n")
        
#         else:
#             # Send a message to the user if the book is't in the inventory
#             print ("Book not found!\n")




#     def display(self) -> None:
#         '''A method to check that the inventory isn't empty abd display it'''
#         if not self.books:
#             print ("Inventory is empty!\n")
#             return
        
#         print ("Current inventory :")
#         for book in self.books:
#             print (f"""Title : {book.title}, Author : {book.author}, 
# ISBN : {book.isbn}, Stock : {book.quantity} copies, 
# Price : ${book.price} per copy""")
#         print ()


# store = ShopInventory() # Create an object of the ShopInventory class

# while True: # Take the choice from the user and handle the cases
#     menu()

#     choice = input("Enter your choice here (1 - 6) :").strip()
#     match choice:

#         case '6':
#             break

#         case '1':
#             title = input("Enter the book title : ").strip().lower()
#             if not check(title,"title"):
#                 continue

#             author = input("Enter the book author : ").strip().lower()
#             if not (author.isalpha()):
#                 print ("The name should be just letters!\n")
#                 continue

#             isbn = input("Enter the ISBN (length : 10) : ").strip()
#             if not ISBN(isbn):
#                 continue

#             quantity = input("Enter the quantity (not less than 1) : ").strip()
#             if not Quantity(quantity):
#                 continue
#             quantity = int(quantity)

#             price = input("Enter the price (not less than 1) : ").strip()
#             if not (price.isdigit()):
#                 print ("Enter a valid price!\n")
#                 continue
#             price = int(price)

#             store.add(title,author,isbn,quantity,price)


#         case '2':
#             isbn = input("Enter the book isbn to check stock : ").strip()
#             if not ISBN(isbn):
#                 continue

#             store.check(isbn)


#         case '3':
#             isbn = input("Enter the ISBN (length : 10) : ").strip()
#             if not ISBN(isbn):
#                 continue

#             quantity = input("Enter the quantity (not less than 1) : ").strip()
#             if not Quantity(quantity):
#                 continue
#             quantity = int(quantity)

#             store.sell(isbn,quantity)


#         case '4':
#             isbn = input("Enter the ISBN (length : 10) : ").strip()
#             if not ISBN(isbn):
#                 continue

#             quantity = input("Enter the quantity (not less than 1) : ").strip()
#             if not Quantity(quantity):
#                 continue
#             quantity = int(quantity)

#             store.restock(isbn,quantity)


#         case '5':
#             store.display()


#         case _:
#             print ("Enter a valid choice!\n")

# print ("Thank you for using the book shop inventory management system, Goodbye!\n")




# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================




# # CrispyTrips
# from statistics import mean , median


# ratings = [] # List to store user-provided ratings

# # Dictionary to keep track of ratings categories : Low(1-2) , Medium(3) , High(4-5)
# ratings_categories = {"low" : 0 , "medium" : 0 , "high" : 0}

# rating_number = 1 # Counter to track the number of ratings entered


# def analyze_satisfaction(ratings : list) -> None:
#     '''Analyze the average and median ratings and display them. If no ratings entered display a message and exit'''
#     if not ratings:
#         print ("\nThere's no ratings! Goodbye.")

#     else:
#         print (f"\nAverage rating : {mean(ratings):.2f}\nMedian rating : {median(ratings):.2f}")

# def add_rating_to_category(rating : int) -> None:
#     '''Update the number of ratings in each category'''
#     if rating <= 2:
#         ratings_categories["low"] += 1
    
#     elif rating == 3:
#         ratings_categories["medium"] += 1

#     else:
#         ratings_categories["high"] += 1

# def rating_percentage(ratings_in_category : int) -> float:
#     '''Calculate the percentage of ratings in each category
#     Args:
#         ratings_in_category(int) : the number of ratings in the category'''
#     return (ratings_in_category / (rating_number - 1)) * 100 if rating_number > 1 else 0

# def analyze_categories() -> None:
#     '''Display the percentage of ratings in each category'''
#     low = ratings_categories["low"]
#     medium = ratings_categories["medium"]
#     high = ratings_categories["high"]

#     low_percentage = rating_percentage(low)
#     medium_percentage = rating_percentage(medium)
#     high_percentage = 100 - (low_percentage + medium_percentage)

#     print (f"Low ratings (1-2) : {low} ({low_percentage:.2f}%)")
#     print (f"Medium ratings (3) : {medium} ({medium_percentage:.2f}%)")
#     print (f"High ratings (4-5) : {high} ({high_percentage:.2f}%)")


# rating = input(f"Enter rating {rating_number} or type 'stop' to end : ").strip()

# # Loop to get ratings from uer until 'stop' is entered
# # Validates the input and update ratings and their categories
# while rating.lower() != "stop":

#     if (not rating.isdigit()) or (int(rating) not in range (1,6)):
#         print ("Invalid rating. Please enter a value between 1 and 5.\n")

#     else:
#         rating = int(rating)
#         ratings.append(rating)
#         add_rating_to_category(rating)
#         rating_number += 1

#     rating = input(f"Enter rating {rating_number} or type 'stop' to end : ").strip()

# # After all ratings are entered
# analyze_satisfaction(ratings)
# analyze_categories()




# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================




# # Managing Library Books


# def is_empty(type : str , name : str) -> bool:
#     '''Check if the user ignored the input.'''
#     if not name:
#         print (f"\nYou shouldn't leave the {type} empty!")
#         return True
#     return False


# def is_book_in_library(title : str , books : list) -> bool:
#     '''Check if the book's entered title is in the library'''
#     return True if any(book['title'] == title for book in books) else False


# def display_choices() -> None:
#     '''Shows the main menu with options for managing the library system.'''
#     print('''
# Library Menu:
# 1. Add a book
# 2. Display books
# 3. Search for a book
# 4. Delete a book
# 5. Update book data
# 6. Exit''')

# class LMS:
#     def __init__(self):
#         self.books = [] # Initialize an empty list to store books in the library.
    

#     def add_book(self, title : str , author : str) -> None:
#         '''Allows the user to add a new book to the library or display a message if the book already exists.'''
#         if is_book_in_library(title , self.books):
#             print (f"\nBook with title: {title}, already exists in the library!")
        
#         else:
#             book = {'title' : title , 'author': author}
#             self.books.append(book)
#             print ("\nBook added successfully.")


#     def display_books(self) -> None:
#         '''Display the all books currently in the library or a message if the library is empty'''
#         if not self.books:
#             print ("\nThe library is empty!")

#         else:
#             print ("\nLibrary books:")
#             for book in self.books:
#                 print(f"Title : {book['title']} , Author : {book['author']}")
        

#     def search_book(self, title : str) -> None:
#         '''Search for a book by its title and display its details or a message if the book not found.'''
#         if is_book_in_library(title , self.books):
#             book = next(book for book in self.books if book['title'] == title)

#             print (f"\nTitle : {title} , Author : {book['author']}")
            
#         else:
#             print ("\nBook not found in the library!")


#     def delete_book(self, title : str) -> None:
#         '''Delete a book by its title or display a message if the book not found.'''
#         if is_book_in_library(title , self.books):
#             self.books = [book for book in self.books if book['title'] != title]
#             print ("\nBook deleted successfully.")
            
#         else:
#             print ("\nBook not found in the library!")


#     def update_book(self, title : str) -> None:
#         '''Update a book's details by its title or display a message if the book not found.'''
#         if is_book_in_library(title , self.books):
#             book = next(book for book in self.books if book['title'] == title)

#             new_title = input("Enter the new title (or press Enter to keep current title) : ").strip()
#             book['title'] = new_title if new_title else title

#             new_author = input("Enter the new author (or press Enter to keep current author) : ").strip()
#             book['author'] = new_author if new_author else book['author']

#             print ("\nBook updated successfully.")
            
#         else:
#             print ("\nBook not found in the library!")

# inventory = LMS()

# # Loop to display the menu and processes user input until the user chooses to exit
# running = True
# while running:
#     display_choices()

#     choice = input("Select an option (1-6) : ").strip()
#     match choice:
#         case '6':
#             print ("\nThanks for using our library system. Goodbye!")
#             running = False

#         case '1':
#             title = input("Enter the book title : ").strip()
#             if is_empty('Title' , title):
#                 continue

#             author = input("Enter the book author : ").strip()
#             if is_empty("Author" , author):
#                 continue

#             inventory.add_book(title , author)

#         case '2':
#             inventory.display_books()

#         case '3':
#             title = input("Enter the title of the book to search : ").strip()
#             if is_empty("Title" , title):
#                 continue

#             inventory.search_book(title)

#         case '4':
#             title = input("Enter the title of the book to delete : ").strip()
#             if is_empty("Title" , title):
#                 continue

#             inventory.delete_book(title)

#         case '5':
#             title = input("Enter the title of the book to update : ").strip()
#             if is_empty("Title" , title):
#                 continue

#             inventory.update_book(title)

#         case _:
#             print ("\nInvalid choice!")




# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================
# ====================================================




# # Paint Coverage Calculator

# def menu() -> None:
#     '''Displays the main menu to the user'''
#     print('''
# Welcome to the Paint Coverage Estimator!
# Regular Paint -> 1210.00 EGP/gallon
# Premium Paint -> 1490.00 EGP/gallon
# Deluxe Paint -> 1580.00 EGP/gallon\n''')

# def paint_type_input() -> str:
#     '''Takes the paint type from the user and returns it as a capitalized string'''
#     return input('Enter (Regular/Premium/Deluxe) or "done" to quit : ').capitalize().strip()

# def is_empty(field_name : str , user_input : str) -> bool:
#     '''Check if the user leaves some input empty. If yes, display a message and return True, else return False'''
#     if not user_input:
#         print (f"You shouldn't leave {field_name} empty!\n")
#         return True
#     return False


# # Paint details.
# PAINT_COVERAGE = {'Regular' : 50 , 'Premium' : 80 , 'Deluxe' : 120}
# PAINT_PRICE = {'Regular' : 1210 , 'Premium' : 1490 , 'Deluxe' : 1580}

# def paint_estimator(paint_type : str , width : float , height : float) -> None:
#     '''Estimate the number of gallons of paint needed and the cost of the paint'''
#     area = width * height
#     gallons_used = area / PAINT_COVERAGE[paint_type]
#     estimated_cost = gallons_used * PAINT_PRICE[paint_type]
#     print (f"You will need {gallons_used:.2f} gallons of {paint_type} Paint"
#            f" to cover a wall of {area:.2f} m^2 The estimated cost is {estimated_cost:.2f} EGP\n")


# def main() -> None:
#     number_of_customers = 0 # Counter to track number of customers.
#     menu()
#     chosen_paint_type = paint_type_input()

#     # Loop to process user input until the user chooses to exit
#     while chosen_paint_type != "Done":

#         if is_empty("Paint Type" , chosen_paint_type):
#             chosen_paint_type = paint_type_input()
#             continue
#         if chosen_paint_type not in PAINT_COVERAGE:
#             print("Invalid paint type! Please try again\n")
#             chosen_paint_type = paint_type_input()
#             continue

#         # Get wall dimensions
#         width = input("Enter the width of the wall in meters : ").strip()
#         if is_empty("Width" , width):
#             chosen_paint_type = paint_type_input()
#             continue
        
#         height = input("Enter the height of the wall in meters : ").strip()
#         if is_empty("Height" , height):
#             chosen_paint_type = paint_type_input()
#             continue
        
#         # Validate that width and height are numbers and > 0
#         try:
#             width = float(width)
#             height = float(height)
#             if width <= 0 or height <= 0:
#                 print ("Width and height must be greater than 0!\n")
#                 chosen_paint_type = paint_type_input()
#                 continue
        
#         except ValueError:
#             print ("Width and height must be numbers!\n")
#             chosen_paint_type = paint_type_input()
#             continue

#         # preform paint estimation
#         number_of_customers += 1
#         paint_estimator(chosen_paint_type , width , height)

#         # Take the next paint type
#         chosen_paint_type = paint_type_input()

#     # After the loop ends
#     print (f"\n{number_of_customers} customers used the program before exiting..")
#     print ("Thank you for using Paint Coverage Calculator!")

# # Start the program
# if __name__ == "__main__":
#     main()
```

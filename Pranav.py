#22/10/19
#Created by Pranav Pandya

x=75
y=35

print("Ex-1:Basic mathematical operations")
print('\n1) Declare two numeric variables and perform basic mathematical operations on it')

print('num1=75, num2=35')
print("Press Y to proceed")
if input()=='y':
    print("Loading...")

print('\nADD     ')
print("The addition opperation for num 1 and num2 is:")
print(x+y)
print("\nSUB     ")
print("The subtraction opperation for num 1 and num2 is:")
print(x-y)

print('\nMUL     ')
print("The multiplication opperation for num 1 and num2 is:")
print(x*y)

print('\nDIV     ')
print("The division opperation for num 1 and num2 is:")
print(x/y)

print('\nPrecentage     ')
print("The precentage of num 1 w.r.t num2 is:")
if x>y:
    print(((x-y)/y)*100)
else:
     print(((y-x)/x)*100)
     
print('\nDIVMOD')
divmod(x,y)

print('\nProceeding to question 2')
print("Press Y to proceed")
if input()=='y':
    print("Loading...")
print('\n2) Declare two numeric variables eg. number1 = 33 and number2 = 55. Interchange the numbers. (number1 = 55 and number2 = 33)')
print("\nProvide your two numbers.\n For exchange operation, numbers have to be distinct.\nIf the numbers are same, then operation will fail")
x=input("Enter your first number")
y=input("Enter your second number")

print("Exchanging values")
if x!=y:
    z=x
    x=y
    y=z
else:
    print("Numbers are same, exchanging will result in no yield")

print("After exchange, num1 is,")
print(x)
print("num2 is")
print(y)

print("Exchange is complete, would you like to proceed?\n Press Y to continue")
if input()=='Y':
    print("We will proceed")
 
print("\nSolve the expression (1/ number1)^2 + (1/number2)^2")
x=input("Input your values for x")
y=input("Input your values for y")
a=float(x)
b=float(y)


print("\nEquation gives output as:",(1/a**2+b**2))
print("\n\nSolve the expression (number1)^5 + (number2)^5")
print("\nEquation gives output as:",(a**5+b**5))
print("\nProceeding to question 3")

print("\n\n3)Write a Python code to read a number from user & find 7th power of it.")
t=input("Input your required number")
u=float(t)
print("The 7th power of that number is",u**7)

print("\nProceeding to question 4")
print("\n\n4) Write a Python code to display welcome message for new students (Welcome to SIG canteen). Take input from user whether a user would like to take Tea or Coffee and display the bill amount of Rs 10 for the item entered by the user.")
print("Welcome to SIG Canteen, all the delicious food you desire are available here.\nSamosas are highly recommended by our students")
print("\n\nWhat would you like to have?\nTEA or\nCOFFEE\nInput your preference below")

menu=input("Tea or Coffee")

if menu=='Tea' or menu=='tea' or menu=='TEA':
    print("Tea costs 10 Rs.")
if menu=='Coffee' or menu=='coffee' or menu=='COFFEE':
    print("Coffee costs 20 Rs.")
    
print("\nProceeding to question 5")
print("\n\n5)Write a Python code to read the name & PRN number of the student and display the note on orientation session.")

print("\nWelcome to SIG")
NAME=input("\nPlease enter your name")
PRN=input("\nPlease enter your PRN:")

print("Hello",NAME,"Welcome to SIG.\nAs mentioned by you, you are assigned PRN number\t",PRN,"and this PRN shall be used for all your academic purposes\nBest of luck")


 
print("6) Write a python code to accept three angles of a triangle and check whether it is a valid triangle or not")
print("Enter your angles")
a1=float (input("Enter angle 1\n"))
a2=float (input("Enter angle 2\n"))
a3=float (input("Enter angle 3\n"))

if (a1+a2+a3)!=180:
    print("Error, not a triangle")
else:
    print("It is a traigle")

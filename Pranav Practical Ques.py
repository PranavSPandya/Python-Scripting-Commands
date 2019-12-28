#1)Take values of length and breadth of a rectangle from user and check if it is square or not.
print("Taking 2 values and checking if it's square or not")
length=float(input("Enter length"))
breadth=float(input("Enter breadth"))

if length==breadth:
          d="does"
else:
          d="doesn't"
print("It ",d,"forms a square")

#2)Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
"""
Rules:
if employee is female, then she will work only in urban areas.
if employee is a male and age is in between 20 to 40 then he may work in anywhere
if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
And any other input of age should print "ERROR".
"""
print("Checking eligilibity to work in Urban or anywhere based on Age, Gender and Marital Status\n")
gen=input("Enter your Gender: Male (M) or Female (F)")
age=int(input("Enter your age"))
marital_status=input("Enter your marital status Yes (Y) or No (N)")

#check
try:
          age>0 or marital_status!=(N or n or y or Y) or gen!=(M or m or f or F)
          
except:
          print("There is error in your data entered, please check and try again")

#Choosing Place of Service
if gen=="F" or gen=="f":
          print("Female can work in Urban Area")

if gen=="M" or gen=="m":
          if (age<=40 and age>20):
                    print("You are eligible to work anywhere")
          if (age<60 and age>40):
                    print("You can work in Urban Areas only")

try:
          age<20 or age>60
except:
          print("ERROR")


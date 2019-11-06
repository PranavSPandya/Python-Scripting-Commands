#Created by Pranav Pandya
#Date 5/11/2019
#Python Script for Factorial Computation

import math


print("1. Write a Python code to accept the number and find the factorial of that number . Use factorial function.")
print("The factorial of your input number is",math.factorial(int(input('Enter your number\n'))))
#The above print command takes the input of a number, converts it into integer and finds factorial of that number
#Input has a higher priority so input will be executed before print command


print("2. Write a Python code to solve the following:\n 1!+2!+3!+4!+5!\n\n")
given_value='1!+2!+3!+4!+5!'
i=0
value_splitted=given_value.split("!+")
#This will split the given string at every "!+"

value=list(value_splitted) 
length=len(value)
value[len-1]=len
j=0

given_list=[]
while j<len(value): #Inserting all string values in a separate list in order to convert it to integer data values
    given_list.insert(j,int(value[j]))
    j=j+1
    
print("The factorial will be parsed and added for numbers",given_list)
i=0
factorial_sum=0
while i<len(value):
    factorial_sum=factorial_sum+math.factorial(given_list[i])
    i=i+1
print("The sum of given string after parsing their factorials is",factorial_sum)
                                                        
print("\n")


print("3. Write a python code to accept three numbers and find the addition of 5 th power of all the numbers. Use math.pow()")

num1=int(input("Enter your first number"))
num2=int(input("Enter your second number"))
num3=int(input("Enter your third number"))

print("Sum of fifth power for all numbers is",math.pow(num1,5)+math.pow(num2,5)+math.pow(num3,5))

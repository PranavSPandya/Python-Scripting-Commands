#Created by Pranav Pandya
#Date 5/11/2019
#code for extracting first character from each name
'''
name=[]
fname=input("Please enter your first name")
mname=input("Please enter your middle name")
lname=input("Please enter your last name")

fname_cap=fname[0].upper()
mname_cap=mname.capitalize()
lname_cap=lname.capitalize()


print(fname_cap[0]+mname_cap[0]+lname_cap[0],fname_cap)

'''
base=float(input("Enter the base value"))
power=float(input("Enter your prompt requirement for power"))

#Power will be calculated in the print command
print("The computed value will be",base**power)

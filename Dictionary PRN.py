'''
#Electives
PRN=[1,2,3,4,5,6,7]
Electives=["Python","GIS","GNSS","Remote Sensing","Photogrammetry"]
electives_PRN=[0,1]
electives_PRN[0]=[Electives[0],Electives[1]]
electives_PRN[1]=[Electives[0],Electives[4]]

PRN_Electives={1907014600+PRN[0]:electives_PRN[0],1907014600+PRN[1]:electives_PRN[1]}
print("The student elective data is",PRN_Electives)


#Code to take input as values and alert if length of name is >9

name=raw_input("Enter your name")

if len(name)>9:
          print("Special Name")
else:
          print("Not Special Name")
'''

#Write a python code to accept the age,gender, marital status from the user
#and display the message as below

#If male/age(5-20)/marital(not married) -> Not eligible to work
#If male/age(20-60) -> Eligilbe to work in urban area
#If male/age(>60) -> Can work only in Hometown

age=int(input("Enter your age"))
marital_status=input("Enter your marital status Yes or No")

if age>=5 and age<20:
          if marital_status=(No or no or NO):
                    print("Not eligible to work")
          else:
                    print("")

if age>=20 and age<60:
                    print("Eligilbe to work in Urban Area")

if age>=60:
          print("Can work only in Home town")
                    

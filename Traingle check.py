#Write a python code to read three angles from user and check wether
#its right abgled traingle or isoceles or equilateral

angle1=float(input("Enter your angle 1"))
angle2=float(input("Enter your angle 2"))
angle3=float(input("Enter your angle 3"))

#Checks for triangle formation by generating an exception

try:
          if((angle1+angle2+angle3)!=180 or angle1<=0 or angle2<=0 or angle3<=0):
                    1/0
except:
          print("It doesn't form a traingle, please enter angles correctly")
          
rd=""
rd2=""
#Checks for 90 degrees and isoceles
if angle1==90 or angle2==90 or angle3==90:
          rd="right angled" #If either angle is 90
          if (angle1==45 and angle2==45) or (angle2==45 and angle3==45) or (angle1==45 and angle3==45):
                    rd2="isoceles triangle" #if either 2 pair of angle is 45
          


elif angle3==60 and angle2==60 and angle1==60:
          rd="equilateral traingle" #If all angles are 60
else:
          rd="normal triangle" #If neither of above but the sum forms a traingle


print("It is a",rd,"",rd2)

import random
import unicodedata

print("Suggesting a secure password")
length=int(input("Enter how many characters long you want the password to be?"))
password=[]
i=0
while i<length:
          if i<=length*.5:
                    z=chr(random.randrange(65,90))
          if (i>length*.5 and i<=length*.8):
                    z=chr(random.randrange(97,112))
          if i>length*.8:
                    z=chr(random.randrange(36,38))
          password.insert(i,z)
          i=i+1
#password_new=password.split(",")

print(password)

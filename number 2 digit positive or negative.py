#Write a python code to Read a numbe from user and check wether it is positive 2 digit number or is a negative 2 digit number

number=int(input("Enter your number"))

if number/100>=1.0 or number/100<0.1:
          print("Please enter two digit number")

else:
          if number >0:
                    print("Entered number is positive two digit")
          else:
                    print("Entered number is negative")

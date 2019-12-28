#created by Pranav Pandya
#Accept Sales and claculate tax amount

print("Enter the sales amount (in number)")
try:
          amount=int(input(""))

except:
          print("Entered value is not a number, please enter quantity of sales in number")

if amount>200000:
          tax=amount*0.05
elif amount>=100000:
          tax=amount*0.02
else:
          tax=amount*0.01

print("your tax amount to be paid is",tax)

print("Google Classroom Problem-1\n")
temperature=float(input("Enter the temperature in degree celsius"))
if temperature < 10:
          print("too too cold")
elif temperature >= 10 and temperature < 20:
          print(" too cold")
elif temperature >=20 and temperature < 25:
          print(" cold")
elif temperature >=25 and temperature < 30:
          print("normal")
elif temperature <35:
          print(" hot")
elif temperature <40:
          print("too hot")
else:
          print("too too hot")

print("Google Classroom Problem-1\n")
print("Program for allocation of Place of Work")
age=int(input("Enter your age"))
gen=input("Enter Gender (M or F)")
marital_status=input("Enter your Marital Status (Y or N)")


if gen =="F":
          print("then she will work only in urban areas")
elif gen=="M" and (age<=20 and age >40):
          print("you may work in anywhere")
elif gen=="M" and (age<=40 and age >60):
          print("you will work in urban areas only")
else:
          print("ERROR")
          








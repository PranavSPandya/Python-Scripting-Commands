'''
1) Python code to read a number from user and find
double factorial of that number
Double factorial is:
if number is even, then mul of 1*2*4*6*8
if number is odd, then mul of 1*3*5*7*9
'''

print('''
Program to get Double Factorial
Double factorial  calculated as:
if number is even, then mul of 1*2*4*6*8
if number is odd, then mul of 1*3*5*7*9
''')
num=int(input("Enter the number for multiplication factorial"))
multiplication_identity=1
numbers=[]
i=0
while num>1:
          i+=1
          multiplication_identity*=num
          numbers.insert(i,num)
          num-=2
numbers_string=str(numbers)
numbers_string=numbers_string.replace(",","*")

print("Your double factorial value",numbers_string, "is",multiplication_identity)
                    
print('''2) Read a number and find sum of cubes of every digit in that number\nEg. if num is 489,then 4^3+8^3+9^3''')
num=int(input("Enter the number for your calculation"))
value=0
list_digits=[]
for digit in str(num):
          value+=int(digit)**3
          list_digits.append(digit)

print("Your sum of cubes of", list_digits,"is",value)




print("Input a name and get it reversed")
name=input("Enter the name")
i=0
name_r=""
for n in name:
          i-=1
          name_r+=name[i]


print("Reversed name is",name_r)
i=0
'''while i<len(name):
          if name[i]==name_r[i]:
                    conclusion="is"
          if name[i]!=name_r[i]:
                    conclusion="is not"
          i+=1
'''
if name==name_r:
          print("Yes")
#print("The given name",conclusion,"a palaindrome")



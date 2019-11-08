#Author - Pranav Pandya
#Date: 1/11/2019
str="Helo"
print (str[0:4],"\n",str[4:],)

print(str[2:4]) #this will print 'll' part of the string
x=len(str)
print (len(str))
i=0
while i<x:
    print (str[i],"\n")
    i=i+1
    
print("\n")

print(type(str))
z=4

print(str)
print("\n\n")
print(str[z-2]) 

print(str[-3:0]) 
print("1")
print(str[-3:])
print("12")
print(str[-2:-1]) 
print("123")
print("\n")
print(str[::])
print(str[::-1])
print(str[::-2])

data=[]
print([range(0,20)])

i=0
while i<20:
    data.insert(i*i,i)
    i+=1
    
print(data)
 



x="etstrstdrdatathonfsdhfoisdhfolijsdoifjdatathonfjasfljaslkf"

z=x.split("datathon")
print (z)

print(len(z))

#Author Pranav Pandya
x=input("Enter number of terms for concatation")
z=int(x)
a=[]
i=0
while i<z:
    a.insert(i,input("Enter value for entry number"))
    i+=1
ranb=input("Enter your concatation range for beginning")
rane=input("Enter your concatation range for ending")

b=int(ranb)
e=int(rane)

#End of program
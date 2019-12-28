#Loops
num=int(input("Enter the number for maths table"))
i=0
while i<16:
          print("|",num,"x",i,"=",num*i,"|")
          i+=1
#Alternate numbers b/w 1 to 100
i=1
alt=0
print("| Alternate numbers|","Odd Numbers","Even Numbers|")
while i<100:
          if i%2==0:
                    alt=i
          print("|",i+2*i,"|",alt-1,"|",alt,"|")
          i=i+1
          

'''
Write a Python code to accept 10 numbers from user using loops and find the average of these numbers.

Write a Python code to find the sum of the 5th power of all the digits of accepted numbers. For example, if number is 786 then sum of the 5th power of all the digits = 7^5 + 8^5 +6^5

Write a Python code to read the number of movie tickets to be booked by the customer and calculate the bill. Rate : Gold - Rs. 220, Silver - Rs. 180, Platinum - Rs. 150. Group discount of 10% is given if group size is greater than 6. Also 2% GST is applied on all the bills.

Write a python code to accept the lower limit and upper limit from the user and count the numbers between the limits. For example if the lower limit is 20 and upper limit is 40 then display the count of numbers between 20 to 40.
'''


print("Ex1")
i=0
num=[]
n=0
while i<10:
          num.append(input("Enter your number"))
          n=n+i
          i+=1

print("Average of those number is",n/i)

print("Ex2")
numeral=input("Enter the number for 5th power sum")
summation=0
for i in str(numeral):
          summation+=int(i)**5

          
print("Summation of 5th power of your number is",summation)



print("Ex3")
print("Enter movie tickets you want to book")
gold=int(input("How many gold tickets? 220Rs./ticket"))
silver=int(input("How many silver tickets? 180Rs./ticket"))
platinum=int(input("How many platinum tickets? 150Rs./ticket"))
discount=0
Total=gold*220+silver*180+platinum*150
if gold+silver+platinum>6:
          discount=0.1
          print("Congratulations, you have availed special discount")
          print("Your discounted amount is Rs.",Total*0.1,"this will be deduced from your billing amount")
gst=0.02
print("Total Money to be paid is\nRs.",Total)
print("Discount of Rs.-",discount*Total)
print("GST added of Rs.+",gst*Total)
print("---------------------------------")
print("Total amount is Rs.",Total-discount*Total+gst*Total)

print("Ex4")
start=int(input("Enter your starting number"))
end=int(input("Enter your ending number"))
count=0
for i in range(start,end+1):
          count=count+1

print("The counted number is",count)



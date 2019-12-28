#Accept age of 2 people and find oldest & youngest

person=[]
print("How many persons age do you know?")
count=int(input(""))

i=0
j=0
#Taking input in list for count number of people
while i<count:
          person.insert(i,input("Please enter age of person "))
          i+=1
          
i=0
same=0
while i<count:
          while j<i:
                    if person[j]==person[i]:
                              same=2+j
                              
                              
                    j+=1
          j=0
          i+=1

           
if same!=0:
          print("\n",same," number of people have same age")
          print("So there is no youngest or oldest amongst them!")
age_sorted=sorted(person)


#if test==0:
if age_sorted[0]!=age_sorted[count-1]:
          print("Youngest person has age",age_sorted[0])
          print("Oldest person has age",age_sorted[count-1])

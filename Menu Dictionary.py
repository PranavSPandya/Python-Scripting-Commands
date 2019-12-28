#1) Create a dictionary which will store the details of the category of the menu item and list of dishes under that menu item

#Created by Pranav Pandya
'''
menu={}

snacks_items=["Idli","Dosa","Mendu Vada"]

soup_items=["Tomato soup","Manchurian soup"]
starter_items=["Veg Kofta","Aloo tikki",soup_items]
main_items=["Paneer Bhurji","Pala paneer","Veg Biryani"]

menu={"snack":snacks_items,"starter":starter_items,"soups":soup_items}

for item in menu:
          for subitem in menu[item]:
                    print(item," has ==>", subitem,"\n")
'''

#2) Read a string from user and replace vowels with dollar
'''
#Think about it late
vowel_value=['a','e','i','o','u']

data=input("Enter your desired value")
i=0
while i<len(data):
          if data[i] in vowel_value:
                    new=data.split(str(i))
                    print(new)
          i+=1
string=""
for splits in data:
          string+=string+"$"

print(string)

'''
'''
vowel_value=['a','e','i','o','u']

data=input("Enter your desired value")
for i in vowel_value:
          data=data.replace(i,"$")


print(data)
'''

#3) Encryption of data
key=['c','a','d','e','i','o','u','z']

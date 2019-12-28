#Accept a month in number and print the number of days in it

month_input=int(input("Enter the month number"))

months=["January","February","March","April","May","June","July","August","September","October","November","December"]
days=[31,28,31,30,31,30,31,31,30,31,30,31]

print("You have provided",months[month_input-1],"which has",days[month_input-1],"days")
           

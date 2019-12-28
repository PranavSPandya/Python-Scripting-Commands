#Created by Pranav Pandya

pop=float(input("Enter the population"))
larea=float(input("Enter the land area"))
density=pop/larea

if pop<10000000:
          print("Low Populated")
          popclass='Low'

else:
          if pop<35000000:
                    print("Moderately Populated")
                    popclass='Med'

if density>=100:
          print("Densely Populated")
          popdens='Densed'
else:
          if density<100:
             print("Sparsely Populated")
             popdens='Sparse'


print("Analysis suggest that\n")

print("|-----------------------------------|")
print("|Population Count|Population Density|")
print("|      ",popclass,"     |     ",popdens,"     |")
print("|-----------------------------------|")





          

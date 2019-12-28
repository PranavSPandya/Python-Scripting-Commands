#Created by Pranav Pandya
#Creating Dictionary with student PRN as keys and List of Electives as values

PRN=[1,2,3,4,5,6,7]
Electives=["Python","GIS","GNSS","Remote Sensing","Photogrammetry"]
print(Electives)
elective_PRN=[]

i=0
j=0
while i < len(PRN):
                   print(PRN[i])
                   elective_count=input("Enter your number of Electives for:")
                   while j<elective_count:
                             elective_PRN.insert([i][j],input("Enter your elective Sr. No."))
                             #elective_PRN[i][j]=input("Enter your elective Sr. No.")
                             j=j+1
                   j=0
                   elective_count=0
                   i=i+1


while i>0:
          student_electives[PRN[i]]=elective_PRNi
          i=i+1

print(student_electives)

# -*- coding: utf-8 -*-
"""
Created by Pranav Pandya
"""
import turtle

n=[490,491,492,493,494,496,497,498,499,500,501,502,504,505,506,507,510,512,513,514,516]

data=[
[492,492,500,498,498,495,497,499,501,502],
[493,497,504,504,504,500,504,504,501,498],
[492,496,504,511,511,508,512,512,502,497],
[491,496,504,507,506,504,501,502,502,497],
[490,496,498,500,499,499,495,494,494,494],
[492,493,496,496,494,493,492,492,491,491],
[494,500,497,497,495,495,495,496,494,494],
[500,507,506,503,500,500,497,495,494,494],
[510,511,512,512,508,500,494,493,494,496],
[514,513,513,509,504,499,494,495,499,501],
[514,516,514,511,506,501,496,499,504,505],
];
i=j=k=a=b=0
turtle.penup()
x=y=[]


while k<len(n):
    k+=1
    while i<10:
              while j<10:
                  if data[j][i]==n[k]:
                      #turtle.goto(i*50,j*50)
                      print(i,j)
                      a=b=a+1
                      
                                            
                  j+=1
              j=0
              i+=1

#plot(x,y)
print(x,y)
print("New")
turtle.penup()
i=j=k=a=b=0
x=y=[]
while k<len(n):
          while i<10:
              while j<10:
                  if data[i][j]==493:
                      turtle.goto(i*50,j*50)
                      print(i,j)
                      x.insert(a,i)
                      y.insert(b,j)
                      a+=1
                      b+=1
                  j+=1
              j=0
              i+=1
          k+=1
print(x,y)
'''
data2=[]
i=j=k=0
while i<10:
    while j<10:
        while k<10:
            if data[j][i]==n[k]:
                data2.insert([j][i],k)
            k+=1
        j+=1
    i+=1
print(data2)


ax =([0,0,10,10]) 
cp = ax.contour(0, 10, 420)
ax.clabel(cp, inline=True, 
          fontsize=10)
ax.set_title('Contour Plot')
ax.set_xlabel('x (cm)')
ax.set_ylabel('y (cm)')
plt.show()
'''

''' 
Author: Kartik Kathuria 
Title: Python Loops
Date: 11-July
Time: 5:33
'''

''' Python For Loops '''
fruits = ["apple", "strawberry", "cherry", "guava","banana","Watermelon"]
for i in fruits:
    print(i)

for x in "banana":
    print(x)

''' Break Statement '''

fruits = ["apple", "strawberry","banana","Watermelon","cherry", "guava",]
for i in fruits:
    print(i)
    if i == "banana":
        break

''' Python Continue Statement'''
fruits = ["apple", "strawberry","banana","Watermelon","cherry", "guava",]
for i in fruits:
    if i == "banana":
        continue
    print(i)

''' range() function'''
for x in range(6): # 0 to (n-1)
    print(x)

for x in range(2,6): # 2 to (6-1)
    print(x)

for x in range(2,30,3): # 2 to (6-1)
    print(x)

''' Else in For  Loop '''
for i in range(6):
    print(i)
else:
    print("Finally Completed")

for i in range(6):
    if i==3: break
    print(i)
else:
    print("Finally Completed!")

''' Nested Loops in Python'''
a = ["vaibhav", "aryan", "vaishnavi"]
b = ["Kartik", "Gaurav", "Ayesha"]

for i in a:
    for j in b:
        print(i,j)

''' Pass Statement'''
for y in [0, 1, 2]:
    pass

''' Python While Loops '''
i = 0
while(i < 6):
    print(i)
    i += 1

''' Break statement in While loop'''
i = 0
while(i < 6):
    print(i)
    if i == 3:
        break
    i += 1

''' Continue statement in While loop'''
i = 0
while(i < 6):
    i += 1
    if i == 3:
        continue
    print(i)

i = 0
while(i < 6):
    print(i)
    i += 1
else:
    print("i is not greater than 6")

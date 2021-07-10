'''
Author: Kartik Kathuria
Class: 5th Class Of Pyrthon and Python Game Development
Student: Vaibhav Suman
Topic: String Slicing, String Concat, String Format, String Modification
'''

# Str = "Hello World"
#  H   e   l   l   o   _   W   o   r   l   d
#  0   1   2   3   4   5   6   7   8   9   10
# -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1                                         
# print(Str[2:5]) # [0:n-1]

# Slicing from the Start
print(Str[:5]) # [0:5-1] or [0:4]

# Slicing to the End
print(Str[6:])

# Negative Indexing
print(Str[-5:-1])  #Str([-num: -num - 1])


''' Python Dor String Modification '''

''' Python Upper() and Lower() Builtin Functions '''
name = "Vaibhav Suman"
print(name)
# Upper() Builtin FUnction
print(name.upper())  #String Modified into UpperCase ('Vaibhav Suman' -->  'VAIBHAV SUMAN')

# Lower() Builtin Function
print(name.lower())  #String modified into LowerCase ('Vaibhav Suman' --> 'vaibhav suman')

''' Python Removing Whitespaces lstrip(), rstrip() and strip() '''
Str1 = "      Hello, Python!         "
print(Str1)
print(Str1.strip())  # combo of lstrip() + rstrip()
print(Str1.lstrip())
print(Str1.rstrip())

''' Python Replace String Builtin Function '''
repString  = "Vartik"
repString1 = "Jaibhav"
print(repString)
print(repString.replace("V", "K"))
print(repString1)
print(repString1.replace("J", "V"))

''' Python Split() String Built-in Function'''

a = "Kartik , Vaibhav, Gaurav, Amit, Hello, World"
print(a.split(","))

name = input("Enter your name:")
print("Good Morning "+name)

name1=input("Enter Grooms name: ")
name2=input("Enter Brides name: ")
print(name1+" Weds "+name2)

''' Python Format Strings '''

name = input("Enter Your Name: ")
age = 19
s = "My name is {}, and I am {} yrs old"
print(s.format(name, age))

s = "I want {} pieces of item {} for {} rupees."

quantities=5
itemno=588
price=98.85
Str="I want {} pieces of item {} for {} rupees."
print(Str.format(quantities,itemno,price))

quantity = 3 #0
itemno = 567 #1
price = 585  #2
myOrder = "I want to pay {2} rupees for {0} pieces of item {1}."
print(myOrder.format(quantity, itemno, price))

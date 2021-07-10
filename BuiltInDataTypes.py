''' Built-in DataTypes 

Text type:           str
Numeric Types:       int, float, complex (a+jb)
Sequence Types:      list, tuple, range
Mapping Types:       dict
Set Types:           set, frozenset
Boolean Types:       bool
Binary types:        bytes, bytearray, memoryview 
'''

a = "Hello, World!"
b = 20
c = 20.5
d = 5 + 6j
e = ['Kartik', 'Vaibhav', 'Aryaman']
f = ("Kartik", "Vaibhav", "Aryaman")
g = range(6)
h = {'name': 'John', 'age': '18'} #dict
i = {"Kartik", "Vaibhav", "Aryaman"}
k = frozenset({"Kartik", "Vaibhav", "Aryaman"})
l = True
m = b"hello"
n = bytearray(5)
o = memoryview(bytes(5))
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(k)
print(l)
print(m)
print(n)
print(o)

'''
Output

Hello, World!
20
20.5
(5+6j)
['Kartik', 'Vaibhav', 'Aryaman']
('Kartik', 'Vaibhav', 'Aryaman')
range(0, 6)
{'name': 'John', 'age': '18'}
{'Vaibhav', 'Kartik', 'Aryaman'}
frozenset({'Vaibhav', 'Kartik', 'Aryaman'})
True
b'hello'
bytearray(b'\x00\x00\x00\x00\x00')
<memory at 0x0000021F65E05940>
'''

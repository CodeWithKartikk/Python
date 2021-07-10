# Python Numbers
# There are three numeric datatypes in Python
# 1. int
# 2. float
# 3. complex

x = 1       # int
y = 5.68    # float
z = 5 + 8j  # complex

print(type(x))
print(type(y))
print(type(z))

'''Casting or Type Casting'''
a = int(5.088)
print(a)
print(type(a))

a = 'e'
b = ord('e')  # ord() function is used to convert char int int.
print(b)      

a = 75
c = chr(75)   # chr() function is used to convert int into char.
print(c)

''' Strings '''

# declare a string 
a = "KARTIK"
print(a)
'''
   K     A    R    T    I    K
   0     1    2    3    4    5
  -6    -5   -4   -3   -2   -1     
'''

# slicing
print(a[1:5])  # (initial pos to (final pos - 1))

a = """Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus eos molestias nisi odit! Adipisci obcaecati ad, cum saepe nihil provident repellendus expedita aut vero numquam earum iste, mollitia molestiae, quae nobis. Cupiditate vero repellendus, in fugit fugiat ipsa deleniti quam omnis repellat expedita voluptatibus nulla praesentium, facere non modi? Deserunt ut quisquam soluta molestiae, ipsa vitae similique fugit laudantium, officia praesentium harum, incidunt cum porro magni distinctio assumenda reiciendis aliquid ab ratione? Voluptate repudiandae earum sunt quo minima inventore reiciendis corporis. Laborum, magni minus facere nostrum excepturi tempore eum nihil dolore sunt nam magnam possimus. Laboriosam, eum laborum porro pariatur, quisquam consequatur officia, hic provident fugiat autem labore? Molestias nulla nisi in perferendis magnam dolore doloribus repellendus corrupti illo a totam eos recusandae at enim fugit, assumenda consequatur sit, debitis hic sapiente blanditiis beatae! Maxime perspiciatis impedit debitis, repellat aliquam voluptas mollitia distinctio delectus in labore voluptatibus dolore dolores doloremque fugit voluptate iste quas. Possimus, at. Nam consequuntur voluptate tempora est, nisi, maxime magni fugiat optio mollitia error harum nesciunt porro, aut ullam quas sequi! Blanditiis dolores eveniet quibusdam excepturi, optio est asperiores necessitatibus ratione dolorem. Fuga praesentium optio facilis laudantium debitis. Aperiam omnis asperiores quis enim consequatur, dolores harum."""
print(a)


# for x in "banana":
#     print(x)

'''

*
* *
* * *
* * * *
* * * * *

* * * * *
*       *
*       *
*       *
*       *
*       *
* * * * *
'''

a = "Hello World"
print(len(a)) # Total Length of the string

''' Pythonn String Methods '''

# -------->  capitalize() --> It converts the first character to uppercase
str = "vaibhav"
cap = str.capitalize()
print(cap)

# -------->  casefold() --> It converts sring into lowercase
str1 = "VaIbHaV"
caf = str1.casefold()
lower = str1.lower()
print(caf)
print(lower)

# -------->  center() --> Returns a centered string 
st = "banana"
a = st.center(50)
print(a)

# -------->  count() --> Returns the no. of times a "specified" value occurs in a string.
str2 = "I love apples, apples are red and apples are my favourite fruit"
cou = str2.count("apple")
print(cou)

# -------->  encode() --> Returns an encoded version of the string.
str3 = "My name is Vaibhav"
enc = str3.encode()
print(enc)

# -------->  endswith() --> Returns True if the string ends with the specified value
str4 = "He is playing Football"
end = str4.endswith("Cricket")
print(end)

# -------->  expandtabs() --> sets the tab size of the string
ext = "H\te\tl\tl\to\t"
tabs = ext.expandtabs(3)
print(ext)
print(tabs)

# -------->  find() --> searches the string for a specufued value and returns the position of where it was found.
ftext = "Hello, welcome to the coding world"
fin = ftext.find("welcome")
print(fin)

# -------->  format() --> formats specified values in a string
formatTxt = "My macbook price is {} rupees"
print(formatTxt.format("85000"))

# -------->  index() --> searches the string for a specufued value and returns the position of where it was found.
itext="Hello, welcome to the coding world."
print(itext.index("Hello"))

# -------->  isalnum()   --> Returns true when all characters in the string is alphanumeric.
cr = "cristiano7"
print(cr.isalnum())

# -------->  isalpha()      --> Returns true when all characters in the string is alphabet.
vi = "virat"
print(vi.isalpha())

# -------->  isdecimal()    --> Returns true when all characters in the string are decimals.
num = "555"
print(num.isdecimal())

# -------->  isdigit()      --> Returns true when all characters in the string are digits.
cr = "cristiano7"
print(cr.isdigit())

# -------->  isnumeric()    --> Returns true when all characters in the string are numeric.
num = "555"
print(num.isnumeric())

# -------->  islower()      --> Returns true when all characters in the string are in lowercase.
lwr = "kartik"
print(lwr.islower())

# -------->  isupper()      --> Returns true when all characters in the string are in uppercase.
upr = "VAIBHAV"
print(upr.isupper())

# -------->  isprintable()  --> Returns true when all characters in the string are prinable.
ipa = "Hello! Are You #1?"
print(ipa.isprintable())

# -------->  isspace()      --> Returns true when all characters in the string are whitespaces.
isp = "     "
print(isp.isspace())

# -------->  istitle()      --> Returns true if the string follows the riule of title.
ist = "Hello, And Welcome To My World!"
print(ist.istitle())

''' join() -> Joins the elements of an iterable to the end of the string (Iteration - Loops) '''

myTuple = ("John", "Peter", "Pope", "Henry")
joinVar = "".join(myTuple)
print(joinVar)

''' ljust() -> It returns the left justified version of the strings '''

txt = "banana"
ljustVar = txt.ljust(20)
print(ljustVar, "is my favorite fruit")

''' rjust() -> It returns the right justified version of the strings '''

txt = "banana"
rjustVar = txt.rjust(20)
print(rjustVar, "is my favorite fruit")

''' lstrip() -> Returns a left trim version of the string'''
''' rstrip() -> Returns the right trim version of the string'''

text = "          banana          "
x = text.lstrip()
y = text.rstrip()
print(x)
print(y)

''' maketrans() -> Returns a translation tableto be used in translation '''
txt = "Hello, Gaurabh"
mytable = txt.maketrans("G","S")
print(txt.translate(mytable))

''' partition() -> FReturns a tuple where the string is parted into three parts '''
partStrVar = "I could drink 3 Glasses of Smoothie"
x = partStrVar.partition("Smooothie")
print(x)

''' replace() -> returns a string where a specified value is with a specified value '''
txt = "I love bananas"
x = txt. replace("bananas", "Apples")
print(x)

''' rfind() -> searches the string for a specified value and returns the last position of where it was found '''
txt = "Mi casa, su casa."
z = txt.rfind("casa")
print(z)

''' rindex() -> searches the string  for a specified value and returns the last position of where it was found'''
txt = "I am Kartik kathuria"
rVar = txt.rindex("kathuria")
print(rVar)

''' splitlines() -> splits the string at line breaks and returns a list'''
txt = " Thank You for the music\nWelcome to My World"
x = txt.splitlines()
print(x)

''' split() -> Splits the string at the specified operaror, and returns a list'''
txt = "Welcome to the jungle"
x = txt.split()
print(x)

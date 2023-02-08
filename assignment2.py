# what is string?
"It represents the text format with single quotes or double quotes"
x = "I love my country"

#what is variable?
"it is used to store data in the variable which means"
x = """i love my country"here" x is a variable and I love my country is stored in variable x"""

#what are parameters?
"the information or data which is store inside the box is defined as parameters"

#what is an integer
"an integer is a value without any decimals"
a = 12345678

#string types
#slicing string

b = "Learning, Python"
print(b[5:])
print(b[8:])
print(b[:6])
print(b[3:12])
print(b[12:5])

print(b[1:16])

#negative index
print(b[-14:-5])
print(b[-1:-12])

#upper case
print(b.upper())
print(b.lower())
print(b.replace("Learn", "driv"))
print(b.split())

#concatenate string
a = "learning"
b = "python"
c = a + b
print(c)

c = a + " " + b
print(c)

#string format

size = 0
quantity = 6
price = 6.6
order = "I want size {} of {} tomatos for the price of{}"
print(order.format(size, quantity, price ))

#escape characters
txt = "I would like to watch \''Bahubali' movie tonight"
print(txt)

txt = "I would like to watch \\'Bahubali' movie tonight"
print(txt)

txt = "I would like to watch \n'Bahubali' movie tonight"
print(txt)
ls
txt= "I would like to watch \r'Bahubali' movie tonight"
print(txt)

txt = "I would like to watch \t'Bahubali' movie tonight"
print(x)





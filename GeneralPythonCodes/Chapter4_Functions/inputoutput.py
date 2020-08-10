''' 
Input and Output in Python
Examples and Playground
'''

print("----------------")

# User Input in Python
uip = input("Enter your name, please : ")
print(uip, "is of type", type(uip))

print("----------------")

# User Input in Python
uip = input("Enter a number, please : ")
print(uip, "is of type", type(uip))

print("----------------")

# User Input to Integer
uip = input("Enter a number, please : ")
x = int(uip)
print(x, "is of type", type(x))

print("----------------")

# User Input to List
uip = input("Enter a list of numbers, please : ")
x = list(uip)
print(x, "is of type", type(x))

print()
for y in x:
    print(10*y)

print("----------------")

# User Input to List
uip = input("Enter a list of numbers, please : ")
x = eval(uip)
print(x, "is of type", type(x))

print()
for y in x:
    print(10*y)

print("----------------")

# Print Output in Python
print("Hello folks! It's almost", 8, "pm.")

print("Hello folks!", end=" ")
print("It's almost", end=" ")
print(8, end=" ")
print("pm.")

print("Hello folks! It's almost {0} pm.".format(8))

print("Hello folks! It's almost {a} pm.".format(a = 8))

print("----------------")

# Complex Format for Print
price_list = {1: 24.5, 2: 34, 3: 105, 4: 234.5, 5: 10}

for item, price in price_list.items():
    print("Item Code: {i:2d},  Price: {p:4.2f}".format(i = item, p = price))

print("----------------")

# -----------------------------------------------
# Quick Tasks
#
# Create a Temperature converter with user input format 32 C to F or 98.6 F to C.
# -----------------------------------------------

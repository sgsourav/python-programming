''' 
Python Dictionaries
Examples and Playground
'''

print("----------------")

# Dictionary in Python
x = { 1: 'Python', 2: 'at', 3: 'NTU' }
print(x)
print(type(x))

print("----------------")

# Elements in a Dictionary
x = { 1: 'Python', 2: 'at', 3: 'NTU' }
print(x)
print(x[1], x[2], x[3])

print("----------------")

# Various types of Keys
x = { 1: 'Python', 'Two': 'at', (3): 'NTU' }
print(x)
print(x[1], x["Two"], x[(3)])

print("----------------")

# Strings as Keys as well as Values
x = { "UCL": "London", "MIT": "Cambridge", "NTU": "Singapore" }
print(x)
print("NTU is located in", x["NTU"])

print("----------------")

# Lists as Values in a Dictionary
x = { "UCL": ["London", 500], "MIT": ["Cambridge", 2000] , "NTU": ["Singapore", 5000] }
print(x)
print("NTU is located in", x["NTU"][0], "and has", x["NTU"][1], "students!")

print("----------------")

# Items, Keys and Values in a Dictionary
x = { "UCL": ["London", 500], "MIT": ["Cambridge", 2000] , "NTU": ["Singapore", 5000] }
print(x)
print(x.items())
print(x.keys())
print(x.values())

print("----------------")

# -----------------------------------------------
# Quick Tasks
#
# Convert the Dictionary {"one" : 1, "two" : 2} to {1 : "one", 2 : "two"}.
# -----------------------------------------------

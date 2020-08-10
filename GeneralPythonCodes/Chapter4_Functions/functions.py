''' 
Functions in Python
Examples and Playground
'''

print("----------------")

# Define a Function
def print_price_list(input_price_list):
    '''prints items and prices from a list'''
    for item, price in input_price_list.items():
        print("Item Code: {i:2d},  Price: {p:4.2f}".format(i = item, p = price))

print(print_price_list)

# Call the Function
price_list = {1: 24.5, 2: 34, 3: 105, 4: 234.5, 5: 10}
print_price_list(input_price_list = price_list)

print("----------------")

# Function that Returns a value
def square(x):
    '''returns the square of a number'''
    return x**2

print(square)
print(square(3))

print("----------------")

# Using a previously defined Function
num_list = [1, 2, 3, 4, 5]
for i in num_list:
    print("Square of {0} is {1}".format(i, square(i)))

print("----------------")

# Using a previously defined Function
num_list = [1, 2, 3, 4, 5]
sqr_list = []
for i in num_list:
    y = square(i)
    sqr_list.append(y)
    
print("Squares of", num_list, "are", sqr_list)

print("----------------")

# Function that Returns multiple values
def maxmin(n_list):
    '''returns maximum and minimum of a list of numbers'''
    list_max = max(n_list)
    list_min = min(n_list)
    return list_max, list_min

print(maxmin)
maxmin([1, 2, 3, 4, 5])

print("----------------")

# Using a multi-value returning Function
num_list = [1, 2, 3, 4, 5]
num_max, num_min = maxmin(num_list)    
print("List :", num_list)
print("Max =", num_max, ",  Min =", num_min)

print("----------------")

# -----------------------------------------------
# Quick Tasks
#
# Create a function for Temperature conversion. Take user input 32 C to F or 98.6 F to C, and use the function to convert the temperature.
# -----------------------------------------------

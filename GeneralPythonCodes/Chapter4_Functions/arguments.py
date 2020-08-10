''' 
Arguments to Functions
Examples and Playground
'''

print("----------------")

# Default Arguments
def log(message = None):
    "logs a message, if passed"
    if message:
        print("LOG: {0}".format(message))
        
print(log)
log("Hello there!")

print("----------------")

# Default Arguments
def greet(name = None):
    "greets a user, if name known"
    if name:
        print("Hello {0}! It's wonderful to meet you.".format(name))

print(greet)        
greet("Sourav")

print("----------------")

# Arbitrary Number of Arguments
def add_n(first_num, *args):
    "returns the sum of one or more numbers"
    num_list = [first_num] + [num for num in args]
    return sum(num_list)

print(add_n)
add_n(1, 2, 3, 4)

print("----------------")

# Arbitrary Number of Arguments
def mult_n(*args):
    "returns the product of one or more numbers"
    result = 1
    for num in args:
        result *= num
    return(result)

print(mult_n)
mult_n(4, 5, 7, 2)

print("----------------")

# -----------------------------------------------
# Quick Tasks
#
# Create a function for Temperature conversion. Take user input 32 C to F or 98.6 F to C, and use the function to convert the temperature. Default conversion should be C to F if the user does not specify.
# -----------------------------------------------

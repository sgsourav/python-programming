''' 
Recursion in Python
Examples and Playground
'''

print("----------------")

# Recursive function : Factorial
def factorial(n):
    '''returns the factorial of an integer'''
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial)
factorial(5)

print("----------------")

# Recursive function : Fibonacci
def fibonacci(n):
    '''returns the n-th fibonacci number'''
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci)
fibonacci(7)

print("----------------")

# Recursive function : Bit-Length
def bitlength(x):
    '''returns the number of bits in an integer'''
    if x == 0 or x == 1:
        return 1
    return 1 + bitlength(x//2)

bitlength(17)

print("----------------")

# -----------------------------------------------
# Quick Tasks
#
# Write a recursive function to sort a List of Numbers using any Sorting Algorithm of your choice.
# -----------------------------------------------

''' 
Basic Python Operations
Examples and Playground
'''

print("----------------")

# Arithmetic Operations

# Addition
print(5 + 2)

# Subtraction 
print(5 - 2)

# Multiplication
print(5 * 2)

# Exact Division
print(5 / 2)

# Quotient
print(5 // 2)

# Remainder
print(5 % 2)

# Exponentiation
print(5 ** 2)

print("----------------")

# Logical Operations

# Equal to
print(5 == 2)

# Not Equal to
print(5 != 2)

# Less than
print(5 < 2)

# Greater than
print(5 > 2)

# Less than or Equal to
print(5 <= 2)

# Greater than or Equal to
print(5 >= 2)

# Logical OR
print(True or False)

# Logical AND
print(True and False)

# Combined Logic
print((5 != 2) or (5 < 2))

# Combined Logic
print((5 >= 2) and (not (5 == 2)))

# Combined Inequality
print(5 > 2 > 1)

# Combined Inequality
print(5 > 2 < 10)

# Combined Logic -- Compute and Print
print( not (True and False), "==", not True or not False)

print("----------------")

# Bitwise Operations

a, b = 5, 2
print('a =', a, "=", bin(a))
print('b =', b, "=", bin(b))
print()   # print blank line

print('a & b =', a & b, "=", bin(a & b))
print('a | b =', a | b, "=", bin(a | b))
print('a ^ b =', a ^ b, "=", bin(a ^ b))

print("----------------")

# -----------------------------------------------
# Quick Tasks
#
# What is the value of (5 != 2) or (5/0 < 2)?
# What is the value of (5 != 2) and (5/0 < 2)?
# -----------------------------------------------

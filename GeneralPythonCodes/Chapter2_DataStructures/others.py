''' 
Python Strings, Tuples and Sets
Examples and Playground
'''

print("----------------")

# String in Python
x = "Singapore"
print(x)
print(type(x))

# Indexing and Slicing
print("The third element  :", x[2])
print("First two elements :", x[:2])
print("Last two elements  :", x[-2:])
print("Concatenate strings:", x + x)
print("Multiply strings   :", 3 * x)

print("----------------")

# -----------------------------------------------
# Quick Tasks
#
# Convert the list ["Python", "is", "a", "fun", "language"] into a single string.
# -----------------------------------------------

print("----------------")

# Tuple in Python
x = (10, 20, 30)
print(x)
print(type(x))

# Indexing and Slicing
print("The third element  :", x[2])
print("First two elements :", x[:2])
print("Last two elements  :", x[-2:])
print("Concatenate tuples :", x + x)
print("Multiply tuples    :", 3 * x)

# -----------------------------------------------
# Quick Tasks
#
# Find the Dot Product (Scalar Product) of the vectors (2, 1, -5) and (3, 0, 10).
# -----------------------------------------------

print("----------------")

# Data Structure Conversion
x = "Singapore"
print(x, "is of type", type(x))
print(list(x), "is of type", type(list(x)))
print(tuple(x), "is of type", type(tuple(x)))

# -----------------------------------------------
# Quick Tasks
#
# Convert the String "Python is a fun language" into a list of the individual words.
# -----------------------------------------------

print("----------------")

# Multiple Simultaneous Assignments
[x, y, z] = ["Python", 3.7, "Singapore"]
print("x =", x, "   y =", y, "   z =", z)
(x, y, z) = ("Python", 3.7, "Singapore")
print("x =", x, "   y =", y, "   z =", z)
x, y, z = "Python", 3.7, "Singapore"
print("x =", x, "   y =", y, "   z =", z)

# -----------------------------------------------
# Quick Tasks
#
# Swap the values of two variables a = 5 and b = 7.
# -----------------------------------------------

print("----------------")

# Set in Python
x = [10, 20, 30, 40, 50]
y = [40, 50, 60, 70]
A, B = set(x), set(y)
print(A)
print(type(A))
print(B)
print(type(B))

# Set Operations
print("Union of Sets :", A.union(B))
print("Set Intersect :", A.intersection(B))
print("Set Difference:", A.difference(B))

# Add or Remove from a Set
A = set([10, 20, 30, 40, 50])
A.add(100)
A.remove(30)
x = A.pop()
print(x, "popped, leaving behind", A)

# Set Relations
A = set([10, 20, 30, 40, 50])
B = set([20,40])
print(A.isdisjoint(B), B.issubset(A), A.issuperset(B))

print("----------------")

# -----------------------------------------------
# Quick Tasks
#
# Remove duplicates from the list [1, 1, 2, 1, 2, 3, 1, 2, 3, 4].
# -----------------------------------------------

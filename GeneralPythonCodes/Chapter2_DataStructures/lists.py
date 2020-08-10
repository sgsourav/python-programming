''' 
Python Lists
Examples and Playground
'''

print("----------------")

# List in Python
x = [10, 20, 30, 40, 50]
print(x)
print(type(x))

print("----------------")

# Indexed Item
print(x[0])

# Negative Indexing
print(x[-1])

print("----------------")

# Slicing a List
print(x[1:3])

# Tail of a List
print(x[1:])

# Head of a List
print(x[:-2])

# Combed Slicing
print(x[1::2])

# Combed Slicing
print(x[:-1:2])

print("----------------")

# List of Characters
x = ["a", "b", "c", "d", "e"]
print(x)
print(type(x))
print(x[2:])

# Mixed Lists
x = [10, "b", 30, "d", 50]
print(x)
print(type(x))
print(x[2:])

print("----------------")

# Lists within Lists (Nested Lists)
x = [10, 20, 30, ["a", "b", "c", "d", "e"]]
print(x)
print(type(x))
print(x[2:])

# Double Indexing in Nested Lists
x = [10, 20, 30, ["a", "b", "c", "d", "e"]]
print(x)
print(type(x))
print(x[3][2:])

# 2D Array with Nested Lists
x = [[1, 2, 3, 4, 5],
     [6, 7, 8, 9, 0],
     [0, 9, 8, 7, 6],
     [5, 4, 3, 2, 1]]
print(x)
print(type(x))
print(x[2][3])

print("----------------")

# List Operations
x = [10, 20, 30, 40, 50]
y = ["a", "b", "c", "d", "e"]
print(x)
print(y)
print("Concatenation:", x + y)
print("List of Lists:", [x] + [y])
print("List of Lists:", [x, y])

# List Functions
x = [10, 20, 30, 40, 50]
y = ["a", "b", "c", "d", "e"]
print("Len:", len(x), len(y))
print("Max:", max(x), max(y))
print("Min:", min(x), min(y))

# List Functions
x = ["It's", "fun", "learning", "python", "at", "NTU"]
print("Max:", max(x))
print("Min:", min(x))
print("Max Len:", max(x, key=len))
print("Min Len:", min(x, key=len))

print("----------------")

# Append to a List
x = [10, 20, 30, 40, 50]
print(x)
x.append(100)
print(x)

# Insert into a List
x = [10, 20, 30, 40, 50]
print(x)
x.insert(3, 100)
print(x)

# Append a List to a List
x = [10, 20, 30, 40, 50]
print(x)
x.append([100, 200, 300])
print(x)

# Extend a List
x = [10, 20, 30, 40, 50]
print(x)
x.extend([100, 200, 300])
print(x)

# Remove from a List
x = [10, 20, 30, 40, 50]
print(x)
x.remove(30)
print(x)

# Pop from a List
x = [10, 20, 30, 40, 50]
y = x.pop()
print(x)
print(y)

print("----------------")

# Copying a List
x = [10, 20, 30, 40, 50]
y = x
print(x)
print(y)

# Copying a List (Wrong)
x = [10, 20, 30, 40, 50]
y = x
x.append(100)
x.remove(30)
print(x)
print(y)

# Copying a List (Right)
x = [10, 20, 30, 40, 50]
y = x[:]
x.append(100)
x.remove(30)
print(x)
print(y)

print("----------------")

# List Arithmetic
x = [10, "NTU"]
print(x + x)
print(3 * x)

print("----------------")

# -----------------------------------------------
# Quick Tasks
#
# Print the list [1, 2, 3, 4, 5] in reverse.
# Create a 10 x 10 array/matrix filled with 1s.
# -----------------------------------------------

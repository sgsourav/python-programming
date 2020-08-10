''' 
Python Iterable Structures
Examples and Playground
'''

print("----------------")

# Loop over a List
some_list = [10, 20, 30, 40, 50]
print(some_list)

for x in some_list:
    print(x**2)

print("Done!")

print("----------------")

# Loop over a List
some_list = ["a", "b", "c", "d", "e"]
print(some_list)

for x in some_list:
    print(10*x)

print("Done!")

print("----------------")

# -----------------------------------------------
# Quick Tasks
#
# Check if there exists a specific number (30, say) in a given list [10, 20, 30, 40, 50].
# -----------------------------------------------

print("----------------")

# Loop over a Range
for x in range(10):
    print(x**2)
    x = x + 1

print("Done!")

print("----------------")

# -----------------------------------------------
# Quick Tasks
#
# Print the Squares of positive numbers below 50 where the Squares are divisible by 3.
# -----------------------------------------------

print("----------------")

# Loop over a List of Lists
list_of_lists = [[1, 2, 3, 4, 5],
                 [6, 7, 8, 9, 0],
                 [0, 9, 8, 7, 6],
                 [5, 4, 3, 2, 1]]
print(list_of_lists)

for a_list in list_of_lists:
    print(3 * a_list)

print("Done!")

print("----------------")

# Nested Loop over a List of Lists
list_of_lists = [[1, 2, 3, 4, 5],
                 [6, 7, 8, 9, 0],
                 [0, 9, 8, 7, 6],
                 [5, 4, 3, 2, 1]]
print(list_of_lists)

for a_list in list_of_lists:
    for x in a_list:
        print(x**2, end="\t")
    print()

print("Done!")

print("----------------")

# -----------------------------------------------
# Quick Tasks
#
# Merge/Flatten a given nested list of lists (may not be equal length sublists) into a single list.
# -----------------------------------------------

print("----------------")

# Loop over a String
some_line = "Python @ NTU Singapore"
print(some_line)

for x in some_line:
    print(x, end=" ")

print("----------------")

# -----------------------------------------------
# Quick Tasks
#
# Check if there is any UPPERCASE character in a given String "Python is Fun!".
# Check if there is any Special Character in a given String "Python is Fun!".
# -----------------------------------------------

print("----------------")

# Loop over a Tuple
some_tuple = (10, 20, 30, 40, 50)
print(some_tuple)

for x in some_tuple:
    print(x**2)

print("Done!")

print("----------------")

# Loop over a Set
some_set = set([10, 20, 30, 40, 50])
print(some_set)

for x in some_set:
    print(x**2)

print("Done!")

print("----------------")

# Loop over all Keys in a Dictionary
some_dict = { "UCL": ["London", 500], "MIT": ["Cambridge", 2000] , "NTU": ["Singapore", 5000] }
print(some_dict)

for x in some_dict.keys():
    print(x)

print("----------------")

# Loop over all Values in a Dictionary
some_dict = { "UCL": ["London UK", 500], "MIT": ["Cambridge", 2000] , "NTU": ["Singapore", 5000] }
print(some_dict)

for x in some_dict.values():
    print(x)

print("----------------")

# Nested Loop over Values in a Dictionary
some_dict = { "UCL": ["London UK", 500], "MIT": ["Cambridge", 2000] , "NTU": ["Singapore", 5000] }
print(some_dict)

for x in some_dict.values():
    for y in x:
        print(y, end="\t")
    print()

print("----------------")

# Loop over all Items in a Dictionary
some_dict = { "UCL": ["London UK", 500], "MIT": ["Cambridge", 2000] , "NTU": ["Singapore", 5000] }
print(some_dict)

for x in some_dict.items():
    print(x)

print("----------------")

# Loop over all (Key, Value) pairs in a Dictionary
some_dict = { "UCL": ["London UK", 500], "MIT": ["Cambridge", 2000] , "NTU": ["Singapore", 5000] }
print(some_dict)

for k, v in some_dict.items():
    print("Key :", k, "\t Value :", v)

print("----------------")

# -----------------------------------------------
# Quick Tasks
#
# Create the list of number of students [500, 2000, 5000] from the dictionary some_dict = { "UCL": ["London UK", 500], "MIT": ["Cambridge", 2000] , "NTU": ["Singapore", 5000] }.
# -----------------------------------------------

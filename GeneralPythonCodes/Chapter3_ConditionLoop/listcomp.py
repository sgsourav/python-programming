''' 
List Comprehension
Examples and Playground
'''

print("----------------")

# Without List Comprehension
num_list = [1, 2, 3, 4, 5]
print(num_list)

sqr_list = []
for x in num_list:
    y = x**2
    sqr_list.append(y)
    
print("Squares of", num_list, "are", sqr_list)

print("----------------")

# With List Comprehension
num_list = [1, 2, 3, 4, 5]
print(num_list)

sqr_list = [x**2 for x in num_list]
print("Squares of", num_list, "are", sqr_list)

print("----------------")

# List Comprehension with Condition
spc_list = [x**2 for x in range(1,50) if x**2 % 3 == 0]
print("List of squares of positive numbers below 50 where the Squares are divisible by 3.")
print(spc_list)

print("----------------")

# -----------------------------------------------
# Quick Tasks
#
# Merge/Flatten a given nested list of lists (may not be equal length sublists) into a single list using list comprehension.
# Create the list of number of students [500, 2000, 5000] from the dictionary some_dict = { "UCL": ["London UK", 500], "MIT": ["Cambridge", 2000] , "NTU": ["Singapore", 5000] } using list comprehension.
# -----------------------------------------------

''' 
Conditional Statements
Examples and Playground
'''

print("----------------")

# IF-ELSE Conditions in Python
x = 5
print('x = ', x)

if x > 3:
    print(x, "is greater than", 3)
else:
    print(x, "is less than or equal to", 3)
    
print("Nice, that seems to work!")

print("----------------")

# Just IF in Python
x = 5
print('x = ', x)

if x > 3:
    print(x, "is greater than", 3)

print("----------------")

# IF-ELIF-ELSE Conditions in Python
x = 5
print('x = ', x)

if x > 3:
    print(x, "is greater than", 3)
elif x < 3:
    print(x, "is less than", 3)
else:
    print(x, "is equal to", 3)
    
print("Nice, that seems to work too!")

print("----------------")

# Nested Conditions in Python
x = 5
print('x = ', x)

if x > 3:
    print(x, "is greater than", 3)
    
    if x < 10:
        print(x, "is less than", 10)
    elif x > 10:
        print(x, "is greater than", 10)
    else:
        print(x, "is equal to", 10)
    
elif x < 3:
    print(x, "is less than", 3)
    
    if x < 0:
        print(x, "is less than", 0)
    elif x > 0:
        print(x, "is greater than", 0)
    else:
        print(x, "is equal to", 0)
    
else:
    print(x, "is equal to", 3)
    
print("Quite nice, again!")

print("----------------")

# -----------------------------------------------
# Quick Tasks
#
# Convert Marks (0 to 100) to Grade 
# A+ (90-100) 
# A (80-89)
# B (70-79) 
# C (60-69) 
# D (50-59) 
# F (< 50)
# -----------------------------------------------

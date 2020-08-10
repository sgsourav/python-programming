''' 
Conditional Iterations
Examples and Playground
'''

print("----------------")

# While Loop
x = 1
while x < 10:
    print(x**2)
    x = x + 1

print("Done!")

print("----------------")

# While Loop
x = 2
while x < 10:
    print(x**2)
    x = x**2

print("Done!")

print("----------------")

# -----------------------------------------------
# Quick Tasks
#
# Print all Fibonacci numbers (1,1,2,3,5,8,13,21,34,...) below 1000.
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
# Print the first 100 Fibonacci numbers (1,1,2,3,5,8,13,21,34,...).
# -----------------------------------------------

print("----------------")

# Break, Pass and Continue
x = 5
print('x = ', x)

while x <= 9:    
    x = x + 1
    
    if x == 8:
        print("first \t", x)
        continue
    else:
        print("second \t", x)
        pass
    
    print("fourth \t", x)

print("last \t", x)

print("----------------")

# Else in a Loop
x = 5
print('x = ', x)

while x <= 9:    
    x = x + 1
    
    if x == 8:
        print("first \t", x)
        continue
    else:
        print("second \t", x)
        pass
    
    print("fourth \t", x)

else:
    print("fifth \t", x)
    
print("last \t", x)

print("----------------")

# -----------------------------------------------
# Quick Tasks
#
# Create a list of all Prime numbers below 100.
# -----------------------------------------------

''' 
Lambda Functions in Python
Examples and Playground
'''

print("----------------")

# Lambda Functions
sqr = lambda x: x * x
print(sqr)
print(sqr(5))

print("----------------")

# Lambda and Map on a List
num_list = [1, 2, 3, 4, 5]
sqr_list = list(map(lambda x: x*x, num_list))
print(sqr_list)
print("Squares of", num_list, "are", sqr_list)

print("----------------")

# Composing Functions
def double(x):
    return 2*x

def square(x):
    return x*x

def f_of_g(f,g):
    "compose two functions"
    return lambda x: f(g(x))

doublesquare = f_of_g(double, square)
print(double)
print(square)
print(doublesquare)
print(doublesquare(3))

print("----------------")

# -----------------------------------------------
# Quick Tasks
#
# Remove punctuations from every word and convert every word to lowercase in the list ["Python,", "quite", "often,", "is", "a", "fun", "Language!"]
# -----------------------------------------------

# =========================================================================== #
# Variants of Division Function created by Sourav Sen Gupta.
# Objective is to learn Python UnitTest using the Divisions.
# =========================================================================== #

# Naive Division
def naive(a, b):
    ''' Naive division function (error-prone)
    ''' 
    return (a / b)

# Safe Division
def safe(a, b):
    ''' Safe division function (robust)
    ''' 
    try:
        return (a / b)
    except:
        return float('inf')

# Correct Division
def correct(a, b):
    ''' Correct division function (robust)
    ''' 
    if b == 0:
        raise ValueError("division by zero is not defined")
    return (a / b)

# =========================================================================== #

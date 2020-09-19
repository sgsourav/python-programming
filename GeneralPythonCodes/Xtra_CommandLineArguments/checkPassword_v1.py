# =========================================================================== #
# Simple Python Script to check the Strength of a Password
# Created by Sourav Sen Gupta to teach Command-Line Inputs
#
# Change the last part of the code to change its behaviour
# =========================================================================== #

# =========================================================================== #
# Function to check the strength of a Password
# This function checks the Password for
# 1. length between 8 and 24,
# 2. at least one uppercase character,
# 3. at least one lowercase character,
# 4. at least one digit,
# 5. at least one special character amongst !@#%&*, and
# 6. no spaces in between.
# Finally, it returns the decision and cause in case of Weak Password.

def isGoodPassword(password):
    ''' Checks whether an input password is 'Good' or 'Bad'.
        input : password (string)
        output : True/False (bool, True if strong password)
        output : Failed conditions (list, empty for Strong)
    '''
    # Sanity check for input
    if not isinstance(password, str):
        return False, ["notString"]

    # Set main parameters and contants
    MINLEN, MAXLEN = 8, 24
    SPECIALCHARSET = "!@#%&*"
    
    # Set a checklist for the desired properties
    checkList = {
                 "matchLen" : False,
                 "hasUpper" : False,
                 "hasLower" : False,
                 "hasDigit" : False,
                 "hasSpcCh" : False,
                 "noSpaces" : True,
                 "noOthers" : True
                }

    # Check the Password for matching length
    passwordLen = len(password)
    if (MINLEN <= passwordLen <= MAXLEN):
        checkList["matchLen"] = True
    
    # Check the Password for other conditions
    for character in password:
        if character.isupper():
            checkList["hasUpper"] = True
        elif character.islower():
            checkList["hasLower"] = True
        elif character.isdigit():
            checkList["hasDigit"] = True
        elif character in SPECIALCHARSET:
            checkList["hasSpcCh"] = True
        elif character.isspace():
            checkList["noSpaces"] = False
        else:
            checkList["noOthers"] = False
        
    # Aggregate the conditions in the checklist
    isValid = (checkList["matchLen"] and 
               checkList["hasUpper"] and 
               checkList["hasLower"] and
               checkList["hasDigit"] and 
               checkList["hasSpcCh"] and
               checkList["noSpaces"] and 
               checkList["noOthers"])
    
    # Return True/False along with failure cause
    failed = [key for key in checkList if checkList[key] == False]
    return isValid, failed

# =========================================================================== #

# Python Script to test the Function
# Run the function with a User Input
password = input("Enter a new password : ")
isGood = isGoodPassword(password)
print(isGood)

# =========================================================================== #

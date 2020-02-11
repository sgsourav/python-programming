# Simple Python Script to check the Strength of a Password
# Change the main() function below to change its behaviour

# Define a Function to check the strength of a Password
def isGoodPassword(password):
    '''
    Checks whether an input password is 'Good' or 'Bad'.
    input : password (string)
    output : True / False (bool)
    '''
    if (len(password) < 8) or (len(password) > 24):
        return False

    hasUpper = False
    hasLower = False
    hasDigit = False
    hasSpcCh = False
    spcChars = "!@#$%^&*"

    for character in password:
        if character.isupper():
            hasUpper = True
        elif character.islower():
            hasLower = True
        elif character.isdigit():
            hasDigit = True
        elif character in spcChars:
            hasSpcCh = True
        elif character.isspace():
            return False
        else:
            return False

    return (hasUpper and hasLower and hasDigit and hasSpcCh)


# Define the main function of this module
def main():
    '''
    Executes the main functionality of the module
    '''
    password = input("Enter a new password : ")
    isGood = isGoodPassword(password)
    print(isGood)


# Run the main function when the script is run
if __name__ == "__main__":
    main()

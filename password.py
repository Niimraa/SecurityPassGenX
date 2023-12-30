
# Import necessary libraries
import random
import string

# Function to shuffle characters in a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)


# Get user input for password length
length = int(input("Enter the password length: "))
password = ""  # Initialize an empty string for the password
j = 1  # Counter for choosing character types in the mixed password

# Check user preferences for password composition
if input("Do you want a mixed password? (if yes, enter 'Y')") == 'Y':
  for x in range(length):
    # Generate characters based on ASCII codes for uppercase, lowercase, digit, and symbol
    if j == 1:
      uppercaseLetter1 = chr(random.randint(65, 90))
      password = password + uppercaseLetter1
      j = j + 1
    elif j == 2:
      lowercaseLetter1 = chr(random.randint(97, 122))
      password = password + lowercaseLetter1
      j = j + 1
    elif j == 3:
      digit1 = chr(random.randint(48, 57))
      password = password + digit1
      j = j + 1
    elif j == 4:
      punctuationSign1 = chr(random.randint(33, 126))
      password = password + punctuationSign1
      j = 1

# Check user preferences for specific character types
elif input("Do you want only an uppercase password?  (if yes, enter 'Y') ") == 'Y':
  for x in range(length):
    uppercaseLetter1 = chr(random.randint(65, 90))
    password = password + uppercaseLetter1

elif input("Do you want only a lowercase password?  (if yes, enter 'Y') ") == 'Y':
  for x in range(length):
    lowercaseLetter1 = chr(random.randint(97, 122))
    password = password + lowercaseLetter1
    
elif input("Do you want only a digit password?  (if yes, enter 'Y') ") == 'Y':
  for x in range(length):
    digit1 = chr(random.randint(48, 57))
    password = password + digit1
    
elif input("Do you want only a symbolic password?  (if yes, enter 'Y') ") == 'Y':
  for x in range(length):
    punctuationSign1 = chr(random.randint(33, 126))
    password = password + punctuationSign1

    #password = uppercaseLetter1 + lowercaseLetter1 + digit1 + punctuationSign1

    
# Shuffle the generated password
password = shuffle(password)

# Output the generated password
print(password)


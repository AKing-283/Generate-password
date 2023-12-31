import string
import random

def generate_pwd(length, use_numbers=True, use_special_chars=True):
    # defining the character sets
    letters = string.ascii_letters
    numbers = string.digits if use_numbers else ""
    special_chars = string.punctuation if use_special_chars else ""

    all_chars = letters + numbers + special_chars
   
    #length of the password should be atleast 1 
    length = max(length, 1)
    
    pwd = ''.join(random.choice (all_chars) for _ in range(length))
    return pwd

#get user inputs
length = int(input("Enter the length of password:  "))
include_numbers = input("Do you want to include numbers in your password (y/n): ").lower()  == 'y'
include_special_chars = input("Do you want to include any special charecter(y/n):").lower()  == 'y'

# Generate the password
pwd = generate_pwd(length, use_numbers=include_numbers, use_special_chars=include_special_chars)
print ("Your generated Password is : ", pwd)
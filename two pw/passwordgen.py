import string
import random

class Gen:
    def __init__(self, pwlen=8):
        # Convert pwlen to an integer if it is not already
        pwlen = int(pwlen)
        
        # Define the source of characters
        s1 = string.ascii_letters  # lowercase and uppercase letters
        s2 = string.digits  # digits 0-9
        s3 = string.punctuation  # punctuation symbols
        
        # Combine the sources into a single string
        s = s1 + s2 + s3
        
        # Generate a random password of length 'pwlen' using the character set 's'
        password = ''.join(random.choice(s) for _ in range(pwlen))
        
        # Print the password
        print(f"Generated password: {password}")

# Create an instance of the Gen class with a desired password length
pw_length = 12  # Example: You can change the password length as needed
gen_instance = Gen(pw_length)

import string
import random

class Gen:
    def __init__(self, pwlen):
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

def main():
    while True:
        try:
            pwlen = int(input("Enter length of password: "))
            if pwlen <= 0:
                print("Password length must be a positive integer. Please try again.")
                continue
            # Create an instance of the Gen class with the provided password length
            gen_instance = Gen(pwlen)
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer value for password length.")

# Run the main function
main()

import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password
def password_generator():
    length = int(input("Enter the desired length for the password: "))  
    if length <= 0:
        print("Password length should be a positive integer.")
    else:     
        password = generate_password(length)
        print(f"Generated Password: {password}")
password_generator()
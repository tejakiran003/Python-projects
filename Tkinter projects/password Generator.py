import random
def process_option(option):
    if option == 'A' or option=='a':
        length = int(input("Enter the length of the password: "))
        alphabets(length)
    elif option == 'B' or option=='b':
        length = int(input("Enter the length of the password: "))
        digits(length)
    elif option == 'C'or option=='c':
        length = int(input("Enter the length of the password: "))
        generate_random(length)
    else:
        print("Invalid option.")

def alphabets(length):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    password = ''.join(random.choice(chars) for _ in range(length))
    print(password)

def digits(length):
    chars = "0123456789"
    password = ''.join(random.choice(chars) for _ in range(length))
    print(password)

def generate_random(length):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    password = ''.join(random.choice(chars) for _ in range(length))
    print(password)
    
print("A:password with only Alphabets   B:password with only digits  C:password with special characters, alphabets, and digits")
option = input("Select an option:")
process_option(option)
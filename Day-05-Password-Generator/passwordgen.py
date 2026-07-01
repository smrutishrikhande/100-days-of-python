import random

# List of letters, symbols, and numbers
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

symbols = ['!', '@', '#', '*', '$', '(', ')']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("🔐 Welcome to the Password Generator!")

# User input
r_letters = int(input("How many letters would you like in your password? "))
r_symbols = int(input("How many symbols would you like? "))
r_numbers = int(input("How many numbers would you like? "))

password_list = []

# Add random letters
for _ in range(r_letters):
    password_list.append(random.choice(letters))

# Add random symbols
for _ in range(r_symbols):
    password_list.append(random.choice(symbols))

# Add random numbers
for _ in range(r_numbers):
    password_list.append(random.choice(numbers))

# Shuffle the password
random.shuffle(password_list)

# Convert list to string
password = "".join(password_list)

print("\nYour generated password is:")
print(password)
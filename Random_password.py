import random

all_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')']

x = int(input("Enter the length of the password "))

password = []

for i in range(x):
    a = random.choice(all_characters)
    all_characters.remove(a)
    password.append(a)

print("".join(password))
    

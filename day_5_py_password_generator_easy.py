import random

print("Welcome to Py Password Generator!\n")

alphabet_list = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

special_chars = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', 
    '[', ']', '{', '}', '\\', '|', ';', ':', '\'', '"', ',', '<', '>', '.', '/', '?'
]

len=int(input("Please Enter the number of characters that the Password should be!\n"))
l=int(input("Enter the no of letters in you want in your Password\n"))
n=int(input("Enter the number of numbers you want in your Password\n"))
s=int(input("Enter the number of special characters you want in your Password\n"))

if l + n + s != len:
    print("\nError: The total count of letters, numbers, and special characters must match the password length!")
else:
    p=""
    for alpha in range(1,l+1):
        p+=random.choice(alphabet_list)
        
    for alpha in range(1,n+1):
        p+=random.choice(number_list)

    for alpha in range(1,s+1):
        p+=random.choice(special_chars)
print(p)

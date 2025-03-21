from day_8_art import logo
print(logo)

def encrypt(text, shift):
    encrypted_text = ""
    for letter in text:
        if letter.isalpha():
            if letter.islower():
                encrypted_text += chr(((ord(letter) - ord('a') + shift) % 26) + ord('a'))
            else:
                encrypted_text += chr(((ord(letter) - ord('A') + shift) % 26) + ord('A'))
        else:
            encrypted_text += letter
    print(f"The encoded text is {encrypted_text}")

def decrypt(text, shift):
    decrypted_text = ""
    for letter in text:
        if letter.isalpha():
            if letter.islower():
                decrypted_text += chr(((ord(letter) - ord('a') - shift) % 26) + ord('a'))
            else:
                decrypted_text += chr(((ord(letter) - ord('A') - shift) % 26) + ord('A'))
        else:
            decrypted_text += letter
    print(f"The decoded text is {decrypted_text}")

choice = input("Enter 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Enter the text to be encrypted/decrypted:\n")
shift = int(input("Enter the shift number:\n"))

if choice == "encode":
    encrypt(text, shift)
elif choice == "decode":
    decrypt(text, shift)
else:
    print("Invalid choice")

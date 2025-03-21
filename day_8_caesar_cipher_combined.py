from day_8_art import logo
print(logo)

def caesar_cipher(text, shift, direction):
    result_text = ""
    if direction == "decode":
        shift *= -1

    for letter in text:
        if letter.isalpha():
            if letter.islower():
                result_text += chr(((ord(letter) - ord('a') + shift) % 26) + ord('a'))
            else:
                result_text += chr(((ord(letter) - ord('A') + shift) % 26) + ord('A'))
        else:
            result_text += letter  
    print(f"The {direction}d text is: {result_text}")

direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()
text = input("Enter the text to be encrypted/decrypted:\n")
shift = int(input("Enter the shift number:\n"))

if direction in ["encode", "decode"]:
    caesar_cipher(text, shift, direction)
else:
    print("Invalid choice")

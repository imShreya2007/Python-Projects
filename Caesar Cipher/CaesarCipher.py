import string

print("Caesar Cipher....")

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase

def caesar_cipher(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == 'decode':
        shift_amount *= -1

    for char in original_text:
        if char in lowercase:
            new_index = (lowercase.index(char) + shift_amount) % 26
            output_text += lowercase[new_index]

        elif char in uppercase:
            new_index = (uppercase.index(char) + shift_amount) % 26
            output_text += uppercase[new_index]

        else:
            output_text += char

    return output_text


should_continue = True

while should_continue:
    direction = input("\nType 'encode' to encrypt or 'decode' to decrypt:\n").lower()

    if direction not in ['encode', 'decode']:
        print("Invalid option. Please choose 'encode' or 'decode'.")
        continue

    text = input("Type your message:\n")
    shift = int(input("Type shift number:\n")) % 26

    result = caesar_cipher(text, shift, direction)
    print(f"\nResult: {result}")

    restart = input("\nType 'yes' to go again, otherwise type 'no':\n").lower()
    if restart == 'no':
        should_continue = False
        print("Goodbye!")

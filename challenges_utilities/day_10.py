# print(ord('A'))
# print(ord('Z'))
# print(ord('a'))
# print(ord('z'))
# print(ord('0'))
# print(ord('9'))

# print(chr(65))
# print(chr(90))
# print(chr(97))
# print(chr(122))
# print(chr(48))
# print(chr(57))


def encrypt(message: str , key: int) -> str:
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        elif char.isdigit():
            encrypted_char = chr((ord(char) - ord('0') + key) % 10 + ord('0'))
        else:
            encrypted_char = char
        encrypted_message += encrypted_char
    return encrypted_message

def decrypt(encrypted_message: str , key: int) -> str:
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - key) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - key) % 26 + ord('a'))
        elif char.isdigit():
            decrypted_char = chr((ord(char) - ord('0') - key) % 10 + ord('0'))
        else:
            decrypted_char = char
        decrypted_message += decrypted_char
    return decrypted_message


message = input("Enter a message: ")
key = int(input("Enter a key: "))
encrypted_message = encrypt(message, key)
print("Encrypted message:", encrypted_message)
decrypted_message = decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)

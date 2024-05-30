'''
Да се реализира на python алгоритъм за шифриране на Цезар. Програмата да приема като входни параметри от командния ред
текст и ключ и да извежда шифрирания текст в конзолата.
'''
import sys


def caesar_cipher(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Expecting 2 arguments: <text> <key>")
        sys.exit(1)

    text = sys.argv[1]
    key = int(sys.argv[2])

    encrypted_text = caesar_cipher(text, key)
    print(encrypted_text)
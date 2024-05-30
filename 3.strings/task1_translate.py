'''
Да се реализира на python алгоритъм за шифриране на Цезар. Програмата да приема като входни параметри от командния ред
текст и ключ и да извежда шифрирания текст в конзолата.
'''
import sys


def caesar_cipher(text, key):
    # Define the lowercase and uppercase alphabets
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Create shifted alphabets
    shifted_lower = lower[key % 26:] + lower[:key % 26]
    shifted_upper = upper[key % 26:] + upper[:key % 26]

    # Create the translation table
    translation_table = str.maketrans(lower + upper, shifted_lower + shifted_upper)

    # Translate the text using the translation table
    encrypted_text = text.translate(translation_table)

    return encrypted_text


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Expecting 2 arguments: <text> <key>")
        sys.exit(1)

    text = sys.argv[1]
    key = int(sys.argv[2])

    encrypted_text = caesar_cipher(text, key)
    print(encrypted_text)
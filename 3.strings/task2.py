'''
Да се реализира на python алгоритъм за шифриране на Виженер. Програмата да приема като входни параметри от командния
ред текст и ключ и да извежда шифрирания текст в конзолата.
'''
import sys
import pdb


def vigenere_cipher(text, key):
    key_length = len(key)
    encrypted_text = ''

    # pdb.set_trace()

    for idx, char in enumerate(text):
        if char.isalpha():
            # selecting char from key, if key is shorter than word - start from the beggining of the key word
            key_char = key[idx % key_length]

            if key_char.islower():
                key_value = ord(key_char) - ord('a') #97
            else:
                key_value = ord(key_char) - ord('A') #65

            if char.islower():
                offset = ord('a') #97
            else:
                offset = ord('A') #65

            text_value = ord(char) - offset
            new_value = (text_value + key_value) % 26
            encrypted_text += chr(new_value + offset)
        else:
            encrypted_text += char

    return encrypted_text


text = 'ATTACKATDAWN'
key = 'LEMON'
encrypted_text = vigenere_cipher(text, key)
print(encrypted_text)

# if __name__ == "__main__":
#     if len(sys.argv) != 3:
#         print("Expecting <text> <key>")
#         sys.exit(1)
#
#     text = sys.argv[1]
#     key = sys.argv[2]
#
#     encrypted_text = vigenere_cipher(text, key)
#     print(encrypted_text)


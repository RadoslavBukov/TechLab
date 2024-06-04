'''
Напишете рекурсивна функция, която връща дали даден символен низ е палиндром (дали низът и обърнатият символен низ са същите).

Програмата трябва да извежда True или False в завимиост от това дали входът е палиндром.
'''
import sys


def is_palindrome(string):
    # if string is only one symbol
    if len(string) <= 1:
        return True
    # Check first and last symbol
    if string[0] != string[-1]:
        return False
    # Recursive calling of the function without first and last symbol
    return is_palindrome(string[1:-1])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Expecting <word>")
        sys.exit(1)

    word = sys.argv[1]

    print(is_palindrome(word))
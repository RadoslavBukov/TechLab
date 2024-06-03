'''
Създайте рекурсивна функция, която при зададено число и степен, връща числото, повдигнато на степента.

Примерен изход при извикване с параметри 2 10:
1024
'''
import sys


def digit_degree(digit, degree):
    if degree == 1:
        return digit

    return digit * digit_degree(digit, degree-1)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Expecting <digit> <degree>")
        sys.exit(1)

    digit = int(sys.argv[1])
    degree = int(sys.argv[2])

    print(digit_degree(digit, degree))
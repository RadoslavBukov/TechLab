'''
Напишете програма, която намира корен на уравнения по метода на дихотомията.
Функцията f(x) да е изнесена в програмна структура функция за леснa промяна.
Числата a и b, които задават интервала на търсене да се въвеждат от клавиатурата. Числата да се четат като символен низ и след това да се конвертират до число.
Ако въведените от потребителя стойности не са числа, както и ако f(a) и f(b) имат един и същ знак да се пораждат съответни изключения.
Търсенето също да е изнесено във функция с име bisection, която получава три параметъра - a, b и функцията за изчисление f(x). След тестване оставете главната програма празна. Функцията bisection трябва да връща резултата с точност 0.001. Тя не трябва да печата нищо.
def f(x):
    return x*x*x+3*x-5


def bisection(a,b, func):
    ...
    ...
    ...
    return ...

print bisection(1,2, f)
Намерете корен на exp(x)-2x-2
Намерете корен на x^3 + 3x-5;
Програмата да е с име XXXXX_L8_T1.py,  където XXXXX е вашето потребителско име в пощата, с която сте регистрирани.
Напишете unit test, който тества функцията за изчисление bisection. Преценете сами какви тестове трябва да съдържа.
Програмата да е с име XXXXX_L8_T2.py,  където XXXXX е вашето потребителско име в пощата, с която сте регистрирани.
Ако формалните изисквания не се спазят, решението не се приема!
'''


class InvalidIntervalError(Exception):
    pass


class NonNumericInputError(Exception):
    pass


def f(x):
    return x ** 3 + 3 * x - 5


def g(x):
    from math import exp
    return exp(x) - 2 * x - 2


def bisection(a, b, func):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise NonNumericInputError("Values must be numbers.")

    if func(a) * func(b) >= 0:
        raise InvalidIntervalError("f(a) and f(b) must have different signs.")

    tolerance = 0.001
    c = a

    while (b - a) / 2 > tolerance:
        c = (a + b) / 2
        if func(c) == 0:
            break
        elif func(a) * func(c) < 0:
            b = c
        else:
            a = c

    return c


def main():
    a = input("Value of a: ")
    b = input("Value of b: ")

    print("Square root of x^3 + 3*x - 5 is:", bisection(a, b, f))
    print("Square root of exp(x) - 2*x - 2 is:", bisection(a, b, g))


if __name__ == "__main__":
    main()








































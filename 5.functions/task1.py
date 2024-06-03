'''
Създайте рекурсивна функция за изчисляване на първите n числа на Фибоначи, и тяхното съхранение в списък.
Реализацията трябва да съхранява вече изчислените стойности, така че когато рекурсивно извикване е с аргумент, който вече е изчислен,
стойността да се взима директно, а да не се изчислява.

Примерен изход при параметри 4 20:
[2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
'''
import sys

# Version 1
# memo = {}
# def fibonacci_recursive(n):
#     if n in memo:
#         return memo[n]
#     if n == 0:
#         memo[n] = 0
#         return memo[n]
#     elif n == 1:
#         memo[n] = 1
#         return memo[n]
#     else:
#         memo[n] = (fibonacci_recursive(n-1) + fibonacci_recursive(n-2))
#         return memo[n]
#
# def print_fibonacci_list(start, end):
#     fibonacci_recursive(end)
#     fibonacci_list = []
#     for i in range(start-1, end):
#         fibonacci_list.append(memo[i])
#     print(fibonacci_list)


# Version 2
def fibonacci_recursive(n, memo):
    if n in memo:
        return memo[n]
    memo[n] = fibonacci_recursive(n-1, memo) + fibonacci_recursive(n-2, memo)
    return memo[n]


def print_fibonacci_list(start, end):
    memory = {0: 0, 1: 1}
    fibonacci_recursive(end, memory)
    fibonacci_list = [memory[i] for i in range(start-1, end)]
    print(fibonacci_list)

# Because dictionaries in Python are mutable, memory and memo refer to the same dictionary object.
# Any changes made to memo inside fibonacci_recursive are reflected in memory outside the function.


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Expecting <start_digit> <end_digit>")
        sys.exit(1)
    start_digit = int(sys.argv[1])
    end_digit = int(sys.argv[2])

    print_fibonacci_list(start_digit,end_digit)
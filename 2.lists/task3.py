'''
Напишете програма, която взима списък и проверява дали който и да е от елементите му се повтаря повече от веднъж.
Вход: XXXXX_L2_T3.py 5 3 1 5 9 2 8 6 7
Изход: True

Входните данни приемайте като параметри от командния ред (виж слайдове "Параметри от командния ред" на презентация 3), а не четете от клавиатурата с input/raw_input

Изходът трябва да е булева стойност, ако има повтарящи се елементи True, False в противен случай
'''
import sys

# has_duplicates v1
def has_duplicates(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return True
        seen.add(item)
    return False

# # has_duplicates v2
# def has_duplicates(lst):
#     # Sorting the collection
#     lst.sort()
#     # Check every element if its equal with the next one
#     for i in range(len(lst) - 1):
#         if lst[i] == lst[i + 1]:
#             return True
#     return False


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No passed arguments")
        sys.exit(1)

    # Taking the arguments from command row, without first one -> ['file.py', 'el1', 'el2']
    input_list = sys.argv[1:]
    print(has_duplicates(input_list))
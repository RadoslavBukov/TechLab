'''
Напишете програма, която взима списък от командния ред и прави нов, в който всеки от елементите на първия се среща точно веднъж.
Вход: XXXXX_L2_T4.py 6 3 7 4 7 4 7 4 8 4 3 8 4 3 8 3 9 4 3
Изход: [3, 4, 6, 7, 8, 9]

Името на изпълнимия файл да е в следния формат: XXXXX_L2_T4.py,  XXXXX е вашето потребителско име в пощата, с която сте регистрирани.

Изходът трябва да е списък от неповтарящи се елементи
'''
import sys


def unique_list(list_input):
    unique_list_elements = []
    for el in list_input:
        if el not in unique_list_elements:
            unique_list_elements.append(el)

    return sorted(unique_list_elements)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No arguments provided.")
        sys.exit(1)

    # Taking the arguments from command row, without first one -> ['file.py', 'el1', 'el2']
    input_list = sys.argv[1:]
    # Check if data is int or str
    input_list = [int(x) if x.isdigit() else x for x in input_list]

    print(unique_list(input_list))
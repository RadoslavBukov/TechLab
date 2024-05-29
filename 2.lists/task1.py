'''
Напишете програма, което проверява дали даден списък е сортиран. Например за списъка ([1,2,2]) програмата ви трябва да казва, че е сортиран,
докато за ('b','a') трябва да казва, че не е сортиран.

Вход: python task1.py 1 2 2
Изход: sorted / unsorted

Входните данни приемайте като параметри от командния ред (виж слайдове "Параметри от командния ред" на презентация 3), а не четете от клавиатурата с input/raw_input
Изходът на файла трябва да е една от двете думи sorted или unsorted
'''
import sys

#Sorting via comparing of each element to the next one
def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No passed arguments")
        sys.exit(1)

    # Taking the arguments from command row, without the first one -> ['file.py', 'el1', 'el2']
    input_list = sys.argv[1:]
    result = is_sorted(input_list)

    if result:
        print("sorted")
    else:
        print("unsorted")
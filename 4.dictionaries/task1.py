'''
Напишете програма, която извежда списък от всички ключове, които сочат към дадена стойност, а ако няма нито една такава стойност,
то да се връща празен списък. Програмата да приема като входен параметър стойността за търсене. Речникът да е статично описан в
кода на програмата и да е следния: d={1:'a',2:'b',3:'c',4:'a',5:'d',6:'e',7:'a',8:'b'}

Примерен изход:
[1, 4, 7]
'''
import sys


def find_keys_by_value(d, value):
    # return [key for key, val in d.items() if val == value]
    keys = []
    for key, val in d.items():
        if val == value:
            keys.append(key)
    return keys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Expecting <value>")
        sys.exit(1)

    search_value = sys.argv[1]

    d = {1: 'a', 2: 'b', 3: 'c', 4: 'a', 5: 'd', 6: 'e', 7: 'a', 8: 'b'}
    keys = find_keys_by_value(d, search_value)

    print(keys)
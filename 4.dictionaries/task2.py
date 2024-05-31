'''
Да се реализира на python програма за създаване на хистограма на честотата на срещане на символите в даден текст.
Програмата да приема като входен параметър текст и да извежда в конзолата съдържанието на речник, съдържащ ключове - символите от текста,
а стойностите  - броя срещания на съответния символ.

Примерен изход:
[('a', 5), ('b', 1), ('c', 1), ('i', 1), ('l', 2), ('n', 1)]
'''
import sys


def histogram(text):
    freq_dict = {}

    for char in text:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1

    sorted_freq_list = sorted(freq_dict.items())
    return sorted_freq_list


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Expecting <text>")
        sys.exit(1)

    input_text = sys.argv[1]
    freq_list = histogram(input_text)

    print(freq_list)
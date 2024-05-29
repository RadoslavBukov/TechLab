'''
Две думи са анаграми ако можем да пренаредим буквите на едната за да напишем другата.
Напишете програма, която проверява дали два символни низа са анаграми.
"Vladimir Nabokov" = "Vivian Darkbloom"
"rocket boys" = "october sky"

Входните данни приемайте като параметри от командния ред (виж слайдове "Параметри от командния ред" на презентация 3), а не четете от клавиатурата с input/raw_input

Резултатът, който трябва да се извежда е низът True, ако думите са анаграми и False в противен случай
'''
import sys


def are_anagrams(str1, str2):
    str1_sorted = sorted(str1.lower())
    str2_sorted = sorted(str2.lower())

    # check if both sorted lists are equal
    return str1_sorted == str2_sorted


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Please provide two string arguments.")
        sys.exit(1)

    str1 = sys.argv[1]
    str2 = sys.argv[2]

    print(are_anagrams(str1, str2))
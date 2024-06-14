'''
Създайте програма, която отваря файл със stem (качен в Moodle) и ги вкарва в речник.
Програмата да получава параметри от командния ред (със sys.argv, не от клавиатурата) име на stem файл и дума.
След попълване на речника да се проверява получената като параметър дума за нейната основна форма и да се извежда резултата в стандартния изход.
'''
import sys


def load_stem_file(file_path):
    stem_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            word, stem = line.strip().split(':')
            stem_dict[word] = stem
    return stem_dict


def find_stem(word, stem_dict):
    if word in stem_dict:
        return stem_dict[word]
    else:
        return "Word not found."


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Not enough arguments.")
    else:
        stem_file = sys.argv[1]
        word = sys.argv[2]

        stem_dict = load_stem_file(stem_file)
        result = find_stem(word, stem_dict)
        print(f"{result}")

# stem_dict = load_stem_file('stemA.txt')
# word = 'Aegeaner'
# result = find_stem(word, stem_dict)
# print(f"Main word form '{word}': {result}")
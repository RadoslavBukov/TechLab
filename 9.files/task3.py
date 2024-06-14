'''
Програма, която отваря текстов файл и го анализира, за да създаде други три файла - един с всички думи,
използвани в текста(по една на ред), един с всички изречения (по едно на ред)
и един с всички биограми (двойки думи със застъпване, които са от едно изречение).
'''
import re


def analyze_text_file(input_file_path):

    with open(input_file_path, 'r') as file:
        text = file.read()

    # Separate sentences
    sentences = re.split(r'(?<=[.!?]) +', text)

    # Separate words
    words = re.findall(r'\b\w+\b', text)

    # biograms
    bigrams = []
    for sentence in sentences:
        tokens = re.findall(r'\b\w+\b', sentence)
        bigrams.extend([f"{tokens[i]} {tokens[i + 1]}" for i in range(len(tokens) - 1)])

    # Words file
    with open('words.txt', 'w') as file:
        for word in words:
            file.write(word + '\n')

    # Sentences file
    with open('sentences.txt', 'w') as file:
        for sentence in sentences:
            file.write(sentence + '\n')

    # Biogram file
    with open('bigrams.txt', 'w') as file:
        for bigram in bigrams:
            file.write(bigram + '\n')


analyze_text_file('input.txt')


'''
Създайте програма, която отваря текстов файл и му сортира редовете, записвайки сортираните редове в друг файл.
Програмата да получава параметри от командния ред (със sys.argv, не от клавиатурата) име на файл за сортиране и име на файл за записване на резултата.
'''
import sys

def sort_file(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()
            # Ensure all lines end with a newline character
            lines = [line if line.endswith('\n') else line + '\n' for line in lines]
            sorted_lines = sorted(lines)

        with open(output_file, 'w') as file:
            file.writelines(sorted_lines)

        print(f"Fail is sorted and saved in {output_file}.")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Not enough arguments.")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        sort_file(input_file, output_file)

# sort_file('forSorting.txt', 'sorted.txt')
'''
Създайте итеративна реализиция на алгоритъма за обхождане на лабиринт. Използвайте списък, за да симулирате програмния стек.
Създайте функция printMaze, която чертае стените с '#', необходеният път с ' ', обходеният в права посока с '.', и в обратна
посока с 'x' и целта с 'g'. Когато целта е постигната, използвайте функцията за да разпечатате текущото състояние на лабиринта.
Функцията за обхождане трябва да се казва solveMaze(x,y) и да приема параметри начални координати на търсенето.
Файлът трябва да приема от командния ред (със sys.argv) начални координати на търсенето в лабиринта.
'''
import sys


maze_init = [
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
    ['|', ' ', '|', ' ', '|', ' ', '|', '|', ' ', '|'],
    ['|', ' ', '|', '|', '|', '|', ' ', '|', ' ', '|'],
    ['|', ' ', '|', '|', ' ', '|', '|', '|', ' ', '|'],
    ['|', ' ', '|', ' ', ' ', ' ', ' ', ' ', 'g', '|'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
]
# maze_init = [
#     ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
#     ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
#     ['#', ' ', '#', ' ', '#', ' ', '#', '#', ' ', '#'],
#     ['#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', '#'],
#     ['#', ' ', '#', '#', '#', '#', ' ', '#', ' ', '#'],
#     ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
#     ['#', ' ', '#', '#', ' ', '#', '#', '#', ' ', '#'],
#     ['#', ' ', '#', ' ', ' ', ' ', ' ', '#', 'g', '#'],
#     ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
# ]


def printMaze(maze):
    for row in maze:
        print('  '.join(row))
    # print()


def solveMaze(maze, initial_x, initial_y):
    if not (0 <= initial_x < len(maze) and 0 <= initial_y < len(maze[0])):
        return False

    current_position = maze[initial_x][initial_y]

    if current_position == 'g':
        printMaze(maze)
        return True

    if current_position in ['-', '|', '.', 'x']:
        return False

    maze[initial_x][initial_y] = '.'

    if solveMaze(maze, initial_x, initial_y + 1) or solveMaze(maze, initial_x, initial_y - 1) or \
        solveMaze(maze, initial_x + 1, initial_y) or solveMaze(maze, initial_x - 1, initial_y):
        return True

    maze[initial_x][initial_y] = 'x'
    return False

# if __name__ == "__main__":
#     if len(sys.argv) != 3:
#         print("Expecting <start_position_x> <start_position_y>")
#         sys.exit(1)
#
#     start_x = int(sys.argv[1])
#     start_y = int(sys.argv[2])
#
#     if maze_init[start_x][start_y] in ['-', '|']:
#         print('Starting coordinates cannot be on a wall.')
#     else:
#         if not solveMaze(maze_init, start_x, start_y):
#             print("No path to destination found.")

solveMaze(maze_init, 1, 1)


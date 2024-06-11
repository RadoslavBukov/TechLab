def is_safe(maze, x, y):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 1


def solve_maze(maze):
    solution = [[0 for _ in range(len(maze[0]))] for _ in range(len(maze))]

    if not solve_maze_util(maze, 0, 0, solution):
        return False, solution
    else:
        return True, solution


def solve_maze_util(maze, x, y, solution):
    # Проверка дали е достигната крайната точка
    if x == len(maze) - 1 and y == len(maze[0]) - 1 and maze[x][y] == 1:
        solution[x][y] = 1
        return True

    # Проверка дали текущата клетка е безопасна за стъпка
    if is_safe(maze, x, y):
        solution[x][y] = 1

        # Стъпка надясно
        if solve_maze_util(maze, x + 1, y, solution):
            return True

        # Стъпка надолу
        if solve_maze_util(maze, x, y + 1, solution):
            return True

        # Ако нито една стъпка не е успешна, връщане назад
        solution[x][y] = 0
        return False

    return False


# Примерен лабиринт (1 представлява проходима клетка, 0 - непреходима)
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

result, solution = solve_maze(maze)

if result:
    print("Пътят е намерен:")
    for row in solution:
        print(row)
else:
    print("Няма път през лабиринта.")

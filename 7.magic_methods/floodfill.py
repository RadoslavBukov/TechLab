# Floodfill recursion function


def flood_fill(matrix, x, y, target_color, replacement_color):
    # Check if target cell is in the matrix size
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
        return

    # Check if current cell is target color
    if matrix[x][y] != target_color:
        return

    # Change color of current cell
    matrix[x][y] = replacement_color

    # Recursive call of neighbour cells
    flood_fill(matrix, x - 1, y, target_color, replacement_color)
    flood_fill(matrix, x + 1, y, target_color, replacement_color)
    flood_fill(matrix, x, y - 1, target_color, replacement_color)
    flood_fill(matrix, x, y + 1, target_color, replacement_color)


matrix = [
    [1, 1, 1, 2, 2],
    [1, 1, 0, 2, 2],
    [1, 1, 3, 1, 2],
    [3, 3, 0, 1, 1],
    [3, 3, 4, 1, 1]
]

x, y = 1, 1
target_color = 1
replacement_color = 9

flood_fill(matrix, x, y, target_color, replacement_color)

for row in matrix:
    print(row)

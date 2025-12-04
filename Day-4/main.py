# Read input from file
with open("input.txt", "r") as file:
    grid = [list(line.strip()) for line in file]

# Variables
rows = len(grid)
cowls = len(grid[0])

"""
(-1, -1), (-1, 0), (-1, 1),
(0, -1),  (  @  )   (0, 1),
(1, -1),  (1, 0),   (1, 1)
"""
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

avaliables = 0

# O(n * m)
for i in range(rows):
    for j in range(cowls):
        if grid[i][j] == "@":
            adjacents = 0

            # New rows and columns, for check the adjacent cells
            for dR, dC in directions:
                newRow = i + dR
                newCow = j + dC

                # Check if the cell is in the grid
                if 0 <= newRow < rows and 0 <= newCow < cowls:
                    if grid[newRow][newCow] == "@":
                        adjacents += 1

            if adjacents < 4:
                avaliables += 1

print(avaliables)

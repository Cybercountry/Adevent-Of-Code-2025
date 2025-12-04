import time


def sleep(seconds):
    time.sleep(seconds)


# Read input from file
with open("input.txt", "r") as file:
    grid = [list(line.strip()) for line in file]

# O((n * m)²)


# Check all cells of the grid
# For any @ in the grid, check the adjacent cells
# If the number of adjacent @ is less than 4, add the cell to the list of rolls available
# The return is a list of tuples containing the coordinates of the cells that can be removed
def find_rolls_available(grid):
    rolls_available = []

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
                    rolls_available.append((i, j))

    return rolls_available


# Variables global
rows = len(grid)
cowls = len(grid[0])
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def main():
    # Variables
    all_removes = 0
    interactions = 0

    # Main loop
    while True:
        rolls = find_rolls_available(grid)

        # Check if there are no more rolls available
        if len(rolls) == 0:
            break

        # Remove the rolls, all operations are executed in memory
        # Rolls has been pre calculated at this point
        for i, j in rolls:
            grid[i][j] = "."

        all_removes += len(rolls)

        print(f"Interaction {interactions}: {len(rolls)} rolls removed")
        for row in grid:
            print("".join(row)[:80])
        sleep(0.25)
        interactions += 1

    print(all_removes)


if __name__ == "__main__":
    main()

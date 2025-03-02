def gridChallenge(grid):
    sorted_rows = [sorted(row) for row in grid]

    for col in range(len(grid[0])):
        for row in range(len(grid) - 1):
            if sorted_rows[row][col] > sorted_rows[row + 1][col]:
                return "NO"

    return "YES"

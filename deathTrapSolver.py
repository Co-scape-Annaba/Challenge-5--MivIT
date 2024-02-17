def mark_skull_platforms(maze, hint):
    def rotate_tiles(tiles, rotation):
        rotated = tiles[:]
        for _ in range(rotation):
            rotated = [rotated[-1]] + rotated[:-1]
        return rotated

    # Iterate through each group of four tiles in the hint matrix
    for i in range(len(hint)):
        for j in range(len(hint[i])):
            symbols = hint[i][j].split(',')
            rotated_symbols = rotate_tiles(symbols, len(symbols) % 4)  # Rotate symbols
            # rotated symbols considered
            if '1' in rotated_symbols:
                maze[i * 2][j * 2] = 'X'
            if '2' in rotated_symbols:
                maze[i * 2][j * 2 + 1] = 'X'
            if '3' in rotated_symbols:
                maze[i * 2 + 1][j * 2] = 'X'
            if '4' in rotated_symbols:
                maze[i * 2 + 1][j * 2 + 1] = 'X'

    return maze


# test
maze = [["T", "T", "T", "T", "T", "T"],
        ["T", "T", "T", "T", "T", "T"],
        ["T", "T", "T", "T", "T", "T"],
        ["T", "T", "T", "T", "T", "T"],
        ["T", "T", "T", "T", "T", "T"],
        ["T", "T", "T", "T", "T", "T"]]

hint = [["2", "3,l", "1,l,l"],
        ["1,r", "2,r,r", "3"],
        ["1,l,l", "3", "2,r"]]

marked_maze = mark_skull_platforms(maze, hint)

# Print the marked maze
for row in marked_maze:
    print(' '.join(row))

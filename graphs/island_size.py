# Battleships in a board
# island size
# largest cities belt with coders, etc.

import sys

# sys.stdin = open("input", "r")
# sys.stdout = open("output", "w")


# 8 neighbors
"""
1 1 1
1 1 1
1 1 1
"""
rows = [-1, -1, -1, 0, 0, 1, 1, 1]
cols = [-1, 0, 1, -1, 1, -1, 0, 1]


''' 
Iterative
'''


def belt_size(grid, r, c):
    current_size = 0
    nodes_to_visit = [(r, c)]

    # DFS
    while nodes_to_visit:
        r, c = nodes_to_visit.pop()

        if grid[r][c]:  # already visited
            grid[r][c] = 0  # mark the city as visited
            current_size += 1

            for k in range(8):
                r_curr, c_curr = r + rows[k], c + cols[k]
                if (
                    0 <= r_curr < len(grid)
                    and 0 <= c_curr < len(grid[0])
                    and grid[r_curr][c_curr]
                ):
                    nodes_to_visit.append((r_curr, c_curr))

    return current_size


def largest_belt(arr, R, C):
    grid = [arr[i: i + C] for i in range(0, len(arr), C)]
    # print(grid)

    result = 0

    for r in range(R):
        for c in range(C):
            if grid[r][c]:
                count = belt_size(grid, r, c)
                result = max(result, count)

    return result


''' 
Recursive
'''


def belt_size(grid, i, j, count):

    grid[i][j] = 0

    for k in range(8):
        r_curr, c_curr = i + rows[k], j + cols[k]
        if (
            (0 <= r_curr < len(grid))
            and (0 <= c_curr < len(grid[0]))
            and grid[r_curr][c_curr]
        ):
            count[0] += 1
            belt_size(grid, r_curr, c_curr, count)


def largest_belt(arr, R, C):
    grid = [arr[i: i + C] for i in range(0, len(arr), R)]
    # print("input:", grid, R, C)
    result = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]:
                grid[i][j] = 0
                count = [1]
                belt_size(grid, i, j, count)
                result = max(result, count[0])

    return result


def main():
    R, C = tuple(int(x) for x in input().strip().split())
    arr = [int(x) for x in input().strip().split()]
    print("largest:", largest_belt(arr, R, C))


if __name__ == "__main__":
    main()

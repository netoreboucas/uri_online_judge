# -*- coding: utf-8 -*-


def scan(start_x, end_x, start_y, end_y):
    global current_max_length

    if start_x >= end_x or start_y >= end_y or (start_x, end_x, start_y, end_y) in processed:
        return 0

    processed.add((start_x, end_x, start_y, end_y))

    if (end_x - start_x) * (end_y - start_y) < current_max_length:
        return 0

    max_length = 0
    current_num = -1000001
    for y in range(start_y, end_y):
        for x in range(start_x, end_x):
            new_num = matrix[y][x]
            if new_num > current_num:
                max_length += 1
                current_num = new_num
            else:
                if y > start_y:
                    max_length -= end_x - start_x - 1
                current_max_length = max(current_max_length, max_length,
                                         scan(start_x, x, start_y, end_y),
                                         scan(x + 1, end_x, start_y, end_y),
                                         scan(start_x, end_x, y + 1, end_y))
                return current_max_length

    current_max_length = max(current_max_length, max_length)
    return current_max_length


while True:
    line = raw_input()
    N, M = map(int, line.split())
    if N == 0 and M == 0:
        break

    matrix = [[int(x) for x in raw_input().split()] for y in range(N)]
    processed = set()
    current_max_length = 0
    scan(0, M, 0, N)
    print current_max_length

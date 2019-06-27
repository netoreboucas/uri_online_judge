# -*- coding: utf-8 -*-


def check(rows, cols, x_dict):
    result = 0

    if cols in x_dict:
        result = min(rows, x_dict[cols])
        rows -= result

    if rows > 0:
        complement_set = set()
        for x in x_dict.keys():
            complement = cols - x
            if complement == x or x not in complement_set and complement in x_dict:
                if complement != x:
                    complement_set.add(complement)
                    count = min(rows, x_dict[x], x_dict[complement])
                    result += 2 * count
                else:
                    count = min(rows, x_dict[x] / 2)
                    result += 2 * count
                rows -= count
                if rows == 0:
                    return result
    else:
        return result

    return None


while True:
    M, N = map(int, raw_input().split())
    if M == 0 and N == 0:
        break

    L = input()
    K = input()
    Xk = [int(x) for x in raw_input().split()]

    max_x = max(N, M)
    x_dict = dict()
    for x in filter(lambda x: x <= max_x, Xk):
        if x in x_dict:
            x_dict[x] = x_dict[x] + 1
        else:
            x_dict[x] = 1

    result_one = check(N * 100 / L, M, x_dict) if N * 100 % L == 0 else None
    result_two = check(M * 100 / L, N, x_dict) if M * 100 % L == 0 else None

    if result_one:
        if result_two:
            print min(result_one, result_two)
        else:
            print result_one
    elif result_two:
        print result_two
    else:
        print 'impossivel'

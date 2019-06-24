# -*- coding: utf-8 -*-

import bisect

case_count = 0
while True:
    case_count += 1
    args = raw_input().split()
    n = int(args[0])
    q = int(args[1])
    if n == 0 and q == 0:
        break

    marbles = []

    for _ in range(n):
        bisect.insort(marbles, int(input()))

    print 'CASE# {}:'.format(case_count)
    for _ in range(q):
        x = int(input())
        y = bisect.bisect_left(marbles, x)
        if y != len(marbles) and marbles[y] == x:
            print '{} found at {}'.format(x, y + 1)
        else:
            print '{} not found'.format(x)

# -*- coding: utf-8 -*-

n = int(input())
for _ in range(n):
    line = raw_input()
    count = 0

    for c in line:
        if c == '0' or c == '6' or c == '9':
            count += 6
        elif c == '1':
            count += 2
        elif c == '2' or c == '3' or c == '5':
            count += 5
        elif c == '4':
            count += 4
        elif c == '7':
            count += 3
        elif c == '8':
            count += 7

    print count,
    print 'leds'

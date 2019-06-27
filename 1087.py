# -*- coding: utf-8 -*-

while True:
    line = raw_input()
    if line == '0 0 0 0':
        break

    x1, y1, x2, y2 = map(int, line.split())
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    if dx == 0:
        if dy == 0:
            print 0
        else:
            print 1
    elif dy == 0 or dx == dy:
        print 1
    else:
        print 2

# -*- coding: utf-8 -*-

while True:
    n = int(input())
    if n == 0:
        break

    line = raw_input().replace(' ', '').replace('1', '')
    mary = len(line)
    john = n - mary
    print 'Mary won {} times and John won {} times'.format(mary, john)

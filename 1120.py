# -*- coding: utf-8 -*-

while True:
    line = raw_input()
    if line == '0 0':
        break

    nums = line.split()
    d = nums[0]
    n = nums[1]

    print long('0' + n.replace(d, ''))

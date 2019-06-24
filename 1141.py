# -*- coding: utf-8 -*-

import sys
sys.setrecursionlimit(100000)

strings = []
maximum_depth = dict()
maximum = 0


def iterate(string, i, m):
    global maximum

    if m > maximum:
        maximum = m

    if i < len(strings) - (maximum - m):
        if string in strings[i]:
            if strings[i] not in maximum_depth or maximum_depth[strings[i]] < m:
                maximum_depth[strings[i]] = m
                iterate(strings[i], i + 1, m + 1)
        iterate(string, i + 1, m)


n = int(input())
while n != 0:
    strings = []
    maximum_depth = dict()
    maximum = 0
    for _ in range(n):
        strings.append(raw_input())

    strings = sorted(set(strings), key=lambda s: len(s))
    iterate('', 0, 0)
    print maximum

    n = int(input())

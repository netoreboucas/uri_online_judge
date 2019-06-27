# -*- coding: utf-8 -*-

try:
    while True:
        a, b = map(long, raw_input().split())
        print a ^ b
except EOFError:
    pass

# -*- coding: utf-8 -*-

n = int(input())
for _ in range(n):
    s_in = raw_input()[::-1]
    s_out = ''
    half = len(s_in) / 2

    for c in s_in[:half]:
        ord_c = ord(c)
        s_out += chr(ord_c + (3 if 65 <= ord_c <= 90 or 97 <= ord_c <= 122 else 0))

    for c in s_in[half:]:
        ord_c = ord(c)
        s_out += chr(ord_c + (2 if 65 <= ord_c <= 90 or 97 <= ord_c <= 122 else -1))

    print s_out

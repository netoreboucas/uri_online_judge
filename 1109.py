# -*- coding: utf-8 -*-

import re

try:
    while True:
        regex = re.compile('^' + raw_input().replace('.', '') + '$')
        p = input()

        for _ in range(p):
            word = raw_input()
            print 'Y' if regex.match(word) else 'N'
        print ''
except EOFError:
    pass

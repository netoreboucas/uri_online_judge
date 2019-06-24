# -*- coding: utf-8 -*-

import re

while True:
    try:
        line = raw_input()
    except EOFError:
        break

    if not line:
        break

    if re.match(r'^\\Tcircle\{[A-Z]\}$', line):
        print 'SIM'
        continue

    valid = True

    treeOpen = 0
    firstChild = False
    secondChild = False
    firstTree = True

    firstChildStack = []
    secondChildStack = []

    i = 0
    line_length = len(line)
    while i < line_length:
        c = line[i]
        if c == '\\':
            if i + 1 < line_length and line[i + 1] == 'T':
                if re.match(r'\\Tcircle\{[A-Z]\}', line[i:i + 11]) and not secondChild and treeOpen > 0:
                    if not firstChild:
                        firstChild = True
                    elif not secondChild:
                        secondChild = True

                    i += 10
                else:
                    valid = False
                    break
            elif i + 1 < line_length and line[i + 1] == 'p':
                if re.match(r'\\pstree\{\\Tcircle\{[A-Z]\}\}\{', line[i:i + 21]) and not secondChild and (firstTree or treeOpen > 0):
                    if not firstChild:
                        firstChild = True
                    elif not secondChild:
                        secondChild = True

                    treeOpen += 1
                    firstChildStack.append(firstChild)
                    secondChildStack.append(secondChild)

                    firstTree = False
                    firstChild = False
                    secondChild = False

                    i += 20
                else:
                    valid = False
                    break
            else:
                valid = False
                break
        elif c == '}' and treeOpen > 0:
            treeOpen -= 1
            firstChild = firstChildStack.pop()
            secondChild = secondChildStack.pop()
        else:
            valid = False
            break
        i += 1

    if treeOpen != 0:
        valid = False

    print 'SIM' if valid else 'NAO'

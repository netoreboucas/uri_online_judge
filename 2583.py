# -*- coding: utf-8 -*-

c = int(input())
for _ in range(c):
    things = set()

    n = int(input())
    for _ in range(n):
        thing, command = raw_input().split()

        if command == 'chirrin':
            things.add(thing)
        elif command == 'chirrion' and thing in things:
            things.remove(thing)

    print 'TOTAL'

    things = sorted(things)
    for thing in things:
        print thing

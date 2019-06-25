# -*- coding: utf-8 -*-

while True:
    n = int(input())
    if n == 0:
        break

    while True:
        line = raw_input()
        if line == '0':
            break

        wagons_out = [int(w) for w in line.split()][::-1]
        station_set = set()
        station_stack = []
        valid = True

        wagons_out_length = n
        station_stack_length = 0

        next_in = 1
        while wagons_out_length > 0 and next_in <= n:
            next_out = wagons_out[-1]
            if next_out not in station_set:
                if next_out != next_in:
                    station_set.add(next_in)
                    station_stack.append(next_in)
                    station_stack_length += 1
                    next_in += 1
                else:
                    wagons_out.pop()
                    wagons_out_length -= 1
                    next_in += 1
            elif station_stack_length > 0 and next_out == station_stack[-1]:
                wagons_out.pop()
                station_stack.pop()
                station_set.remove(next_out)
                wagons_out_length -= 1
                station_stack_length -= 1
            else:
                valid = False
                break

        if valid and wagons_out_length > 0 and wagons_out_length == station_stack_length:
            for i in range(wagons_out_length):
                if wagons_out[i] != station_stack[i]:
                    valid = False
                    break

        print 'Yes' if valid else 'No'
    print ''

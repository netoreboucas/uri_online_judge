# -*- coding: utf-8 -*-


def mdc(num1, num2):
    rest = -1
    while rest != 0:
        rest = num1 % num2
        num1 = num2
        num2 = rest
    return num1


n = int(input())
for _ in range(n):
    parts = raw_input().split()

    n1 = int(parts[0])
    d1 = int(parts[2])
    n2 = int(parts[4])
    d2 = int(parts[6])

    if parts[3] == '+':
        n = n1 * d2 + n2 * d1
        d = d1 * d2
    elif parts[3] == '-':
        n = n1 * d2 - n2 * d1
        d = d1 * d2
    elif parts[3] == '*':
        n = n1 * n2
        d = d1 * d2
    elif parts[3] == '/':
        n = n1 * d2
        d = n2 * d1

    mdc_result = mdc(n, d)
    print '{}/{} = {}/{}'.format(n, d, n / mdc_result, d / mdc_result)

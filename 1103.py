# -*- coding: utf-8 -*-

while True:
    nums = raw_input().split()
    t1 = int(nums[0]) * 60 + int(nums[1])
    t2 = int(nums[2]) * 60 + int(nums[3])

    if t1 == 0 and t2 == 0:
        break

    if t1 >= t2:
        t2 += 1440

    print t2 - t1

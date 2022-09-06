#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    uniq_list = list(set(my_list))
    for num in uniq_list:
        sum += num
    return sum

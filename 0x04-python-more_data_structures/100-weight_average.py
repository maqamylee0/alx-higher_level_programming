#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum_avg = 0
    total_weight = 0
    for score, weight in my_list:
        sum_avg += score * weight
    total_weight = sum(map(lambda x: x[1], my_list))
    return sum_avg / total_weight

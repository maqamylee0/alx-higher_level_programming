#!/usr/bin/python3
def best_score(a_dictionary):
    highest = 0
    high_key = None
    if not a_dictionary:
        return None
    for key, value in a_dictionary.items():
        if value > highest:
            highest = value
            high_key = key
    return high_key

#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    deletion = []
    for key, val in a_dictionary.items():
        if value == val:
            deletion.append(key)
    for key in deletion:
        del a_dictionary[key]
    return a_dictionary

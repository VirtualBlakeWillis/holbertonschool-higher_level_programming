#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best = list(a_dictionary.items())[0][0]

    for key in a_dictionary:
        if a_dictionary[key] > a_dictionary[best]:
            best = key

    return best

#!/usr/bin/python3
def roman_to_int(roman_string):
    final = 0
    roman_to_int = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000}

    if not roman_string or type(roman_string) != str:
        return None

    for idx in range(len(roman_string) - 1):
        current = roman_string[idx]
        next = roman_string[idx + 1]

        if roman_to_int[next] > roman_to_int[current]:
            final -= roman_to_int[current]
        else:
            final += roman_to_int[current]

    final += roman_to_int[roman_string[-1]]
    return final

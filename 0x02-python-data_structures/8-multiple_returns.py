#!/usr/bin/python3
def multiple_returns(sentence):
    str_len = len(sentence)
    if sentence == "":
        first = None
    else:
        first = sentence[0]

    return (str_len, first)

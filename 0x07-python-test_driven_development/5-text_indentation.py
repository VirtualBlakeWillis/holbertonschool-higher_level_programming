#!/usr/bin/python3
def text_indentation(text):

    char_list = [".", "?", ":"]
    if type(text) is not str:
        raise TypeError("text must be a string")
    
    for char in text:
        print(char, end="")
        for comp in char_list:
            if char is comp:
                print("\n\n", end="")
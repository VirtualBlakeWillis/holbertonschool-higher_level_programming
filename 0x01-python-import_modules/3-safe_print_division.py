#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        final = a / b
    except:
        final = None
    finally:
        print("Inside Result: {}".format(final))
        return final

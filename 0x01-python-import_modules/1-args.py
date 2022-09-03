#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    args = len(argv) - 1
    i = 0

    if args == 1:
        arg_str = "argument"
    else:
        arg_str = "arguments"

    if args == 0:
        punc = "."
    else:
        punc = ":"

    print("{:d} {:s}{:s}".format(args, arg_str, punc))

    for i in range(1, len(argv)):
        print("{:d}: {:s}".format(i, argv[i]))

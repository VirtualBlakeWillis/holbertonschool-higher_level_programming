#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    args = len(argv) - 1
    punc = ":"
    i = 0

    if args == 1:
        arg_str = "argument"
    elif args == 0:
        punc = "."
    else:
        arg_str = "arguments"

    print("{:d} {:s}{:s}".format(args, arg_str, punc))

    for i in range(1, len(argv)):
        print("{:d}: {:s}".format(i, argv[i]))

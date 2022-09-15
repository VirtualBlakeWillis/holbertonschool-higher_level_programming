#!/usr/bin/python3
""" class inheritence """


class MyList(list):
    """ sort, then print """

    def print_sorted(self):
        self.sort()
        print(self)

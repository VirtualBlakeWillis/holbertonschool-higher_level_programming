#!/usr/bin/python3
for i in range(8):
    for x in range(10):
        if x > i:
            print("{:d}{:d}".format(i, x), end=", ")
print("89")

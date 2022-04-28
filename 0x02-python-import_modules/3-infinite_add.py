#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)
    sum = 0
    for n in range(1, length):
        nextnum = int(argv[n])
        sum += nextnum
        print("{}".format(sum))

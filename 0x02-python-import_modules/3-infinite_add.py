#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)
    sum = 0
    for n in range(1, length):
        num = int(argv[n])
        sum += num
        print("{}".format(sum))

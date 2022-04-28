#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    leng = len(argv)
    sum = 0
    for j in range(1, leng):
        num = int(argv[j])
        sum += num
    print("{}".format(sum))

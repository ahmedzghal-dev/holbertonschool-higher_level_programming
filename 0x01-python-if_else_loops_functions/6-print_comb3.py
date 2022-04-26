#!/usr/bin/python3
for n in range(0, 10):
    for j in range(0, 10):
        if n < j:
            if n < 8:
                print("{}{},".format(n, j), end=" ")
            else:
                print("{}{}".format(n, j))

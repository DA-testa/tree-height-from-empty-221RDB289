# python3
# Autors: Gundars Pelle 6. grupa

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    # Your code here

    tree = [[] for _ in range(n)]

    i = 0
    for parent in parents:
        if parent != '-1':
            tree[int(parent)].append(i)
        else:
            root = i
        i += 1

    stack = [(root, 0)]
    max_height = 0
    while stack:
        node, height = stack.pop()

        if height > max_height:
            max_height = height

        for child in tree[node]:
            stack.append((child, height + 1))

    return max_height + 1


def main():
    # implement input form keyboard and from files
    mode = input()
    if mode.startswith('I'):
        # input number of elements
        n = int(input())
        # input values in one variable, separate with space, split these values in an array
        values = input().split(' ')

        # call the function and output it's result
        print(compute_height(n, values))
    elif mode.startswith('F'):
        # let user input file name to use, don't allow file names with letter a
        # account for github input inprecision
        file_name = input()
        if 'a' not in file_name:
            f = open('test/'+file_name, 'r')
            text = f.read().split('\n')
            f.close()
            # input number of elements
            n = int(text[0])
            # input values in one variable, separate with space, split these values in an array
            values = text[1].split(' ')

            # call the function and output it's result
            print(compute_height(n, values))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# python3
# Autors: Gundars Pelle 6. grupa

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    # Your code here

    v = parents # values
    h = numpy.zeros(n) # heights
    c = numpy.zeros(n) # checked nodes

    i = 0
    while 0 <= i and i <= n-1:
        temp = []
        j = i
        increase = None
        while(True):
            if int(v[j]) == -1:
                increase = 1
                break
            elif c[j] == 2:
                increase = h[j]
                break
            elif c[j] == 1 or c[j] == 0:
                temp.append(j)
                for t in temp:
                    if c[t] != 2:
                        h[t] += 1
                j = int(v[j])
                
        if increase:
            for t in temp:
                if c[t] == 1 or c[t] == 0:
                    c[t] = 2
                    h[t] += increase

        i+=1


    return int(numpy.max(h))


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
main()
# print(numpy.array([1,2,3]))
 #!/usr/bin/python
# There are N integers in an array A. All but one integer occur in pairs. Your task is to find out the number that occurs only once.
# 
# The first line of the input contains an integer N indicating the number of integers. 
# The next line contains N space separated integers that form the array A.
# 
# Output S, the number that occurs only once.

import sys

DEBUG = False

if (DEBUG): fp=open('input.txt')

def print_debug(str):
    if (DEBUG): print "DEBUG: " + str
    return

def read_input():
    if (DEBUG):
        ret=map(int, fp.readline().split(' '))
    else:
        ret=map(int, sys.stdin.readline().split(' '))
    return ret

def main():
    N = read_input()
    A = read_input()
    d = {}

    for i in A:
        if i in d:  d[i] = d[i]+1
        else:       d[i] = 1
    print d.keys()[d.values().index(1)]

if __name__ == '__main__':
    main()

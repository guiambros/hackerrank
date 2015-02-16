 #!/usr/bin/python
# -*- coding: UTF-8 -*-
#
import sys

DEBUG = True

if (DEBUG): fp=open('input1.txt')

def print_debug(str):
    if (DEBUG): print "DEBUG: " + str
    return

def read_input():
    if (DEBUG):
        ret=map(int, fp.readline().split(' '))
    else:
        ret=map(int, sys.stdin.readline().split(' '))
    return ret

def print_array(a):
    print " ".join("%d" % i for i in a)

def main():
    s = int(read_input()[0])
    a = read_input()
    p, array = a[0], a[1:]
    right, left = [], []
    for i in array:
        if i>p:
            right.append(i)
        else:
            left.append(i)

    print_array(left + [p] + right)

if __name__ == '__main__':
    main()

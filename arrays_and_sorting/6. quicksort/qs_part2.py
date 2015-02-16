 #!/usr/bin/python
# -*- coding: UTF-8 -*-
#
import sys

DEBUG = True

if (DEBUG): fp=open('input2.txt')

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
    quicksort(a)

def quicksort(a):
    if len(a) < 2:
        return a
    pv = a[0]
    left, right = partition(a)
    l = quicksort(left)
    r = quicksort(right)
    ret = l + [pv] + r
    print_array(ret)
    return ret

def partition(a):
    p = a[0]
    array = a[1:]
    right, left = [], []
    for i in array:
        if i>p:
            right.append(i)
        else:
            left.append(i)    
    return(left, right)

if __name__ == '__main__':
    main()

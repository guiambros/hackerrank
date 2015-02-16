 #!/usr/bin/python
# -*- coding: UTF-8 -*-
#
import sys

DEBUG = True

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

def print_array(a):
    print " ".join("%d" % i for i in a)

def main():
    s = int(read_input()[0])
    a = read_input()
    a_tosort = []
    a_tosort.append(a[0])
    for pos in range(1, s):
        a_tosort.append(a[pos])
        a_sorted = insertion_sort_broken(a_tosort)
        #print "sorted  = %s, unsorted = %s" % (a_sorted, a[pos+1:])
        #print_array (a_sorted + a[pos+1:])
        print_array (a_sorted)

def main2():
    s = int(read_input()[0])
    a = read_input()
    insertion_sort_broken(a)
    print " ".join(map(str,a))


# Receives a pre-sorted array with only the last element *possibly* out of
# order, and re-orders it, if needed
def insertion_sort(a):
    s = len(a)
    v = a[s-1]
    for pos in range(s-1, 0, -1):
        prev = pos-1
        if a[pos] < a[prev]:
            a[pos],a[prev] = a[prev],a[pos]
    return a

def insertion_sort_broken(a):
    for pos in xrange(1, len(a)):
        prev = pos-1 
        key = a[pos]
        while (a[prev] > key and prev>-1):
           a[prev+1] = a[prev]
           prev -= 1
        a[prev+1] = key
    return a

if __name__ == '__main__':
    main()

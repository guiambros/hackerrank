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
    a_sorted, count = insertion_sort(a)
    #print_array (a_sorted)
    print (count)

def insertion_sort(a):
    count=0
    for pos in xrange(1, len(a)):
        prev = pos-1 
        key = a[pos]
        while (a[prev] > key and prev>-1):
           count+=1
           a[prev+1] = a[prev]
           prev -= 1
        a[prev+1] = key
    return a, count

if __name__ == '__main__':
    main()

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
    v = a[s-1]
    cur = prev = 0
    for i in range(0, s+1):
        cur = s-i-1
        prev = cur-1
        if ((cur==0) or (a[prev] < v and v < a[cur])):
            a[cur] = v
            break
        a[cur] = a[prev]
        print_array(a)
    
    print_array(a)

if __name__ == '__main__':
    main()

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

def main():
    v = int(read_input()[0])
    n = int(read_input()[0])
    array = sorted(read_input())

    try:
        print array.index(v)
    except ValueError:
        print -1

if __name__ == '__main__':
    main()

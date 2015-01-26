 #!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# Given two integers: L and R, find the
# maximal values of A xor B given, L <= A ≤ B ≤ R
#
# https://www.hackerrank.com/challenges/maximizing-xor

import sys

def  maxXor( l,  r):
    maxXor = 0
    for outer in range(l, r+1):
        for inner in range(outer, r+1):     # a xor b == b xor a. So we don't need
            xor = outer^inner               # to search the entire l <=> r space.
            if xor > maxXor:                # Only from outer <=> r)
                maxXor = xor

    return maxXor

def read_multiline_input():
    return(sys.stdin.readlines())

def main(lines=[]):
    if (len(lines)==0): lines = read_multiline_input()

    if len(lines)!=2:
        print "Wrong number of input lines: %d" % (len(lines))
    else:
        l = int(lines[0])
        r = int(lines[1])
        print maxXor(l, r)

    return

def test():
    test_list = [ 10, 13]
    main(test_list)

if __name__ == '__main__':
    main()

 #!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# Bill Gates is on one of his philanthropic journeys to a village in Utopia. He
# has N packets of candies and would like to distribute one packet to each of
# the K children in the village (each packet may contain different number of
# candies). To avoid any fighting among the children, he would like to pick ANY
# K-packets, out of his N packets, such that unfairness is minimized.
#
# Suppose the K packets have (x1, x2, x3,....xk) candies in them, where xi
# denotes the number of candies in the ith packet, then we define unfairness as
#
#      max(x1,x2,...xk) - min(x1,x2,...xk)
#
# where max denotes the highest value amongst the elements, and min denotes the
# least value amongst the elements. Can you figure out the minimum unfairness
# and print it?
#
# INPUT:
# The first line contains an integer N.
# The second line contains an integer K. N lines follow. Each line contains
# an integer that denotes the candy in the nth (1≤n≤N) packet.
#
# OUTPUT:
# An integer that denotes the minimum possible value of unfairness.
#
# SAMPLE:
# 6
# 3
# 10
# 20
# 30
# 100
# 101
# 102
#
# Res = 2 (why? max(100,101,102)-min(100, 101, 102))
#
# https://www.hackerrank.com/challenges/angry-children


import sys
DEBUG = None

def print_debug(str):
    if (DEBUG): print "DEBUG: " + str
    return

def search_min_unfair(array, k):
    if (len(array)<k): return                # invalid

    min_unfairness = 1<<31
    array.sort()
    
    for i in range(0, len(array)-k+1):
        # not needed! pktslice = array[i:i+k]
        # A (much) faster solution: min = array[i], max = array[i+k]
        this_unfairness = array[i+k-1]-array[i]
        if this_unfairness<min_unfairness:
            min_unfairness = this_unfairness
    return min_unfairness

def read_multiline_input():
    return(sys.stdin.readlines())

def main(lines=[]):
    if (len(lines)==0): lines=read_multiline_input()
    N = int(lines[0])
    k = int(lines[1])
    print_debug("len(N) = %d, k = %d" % (N, k))
    packets = map(int, lines[2:])   # convert list of strings to int
    unfairness = search_min_unfair(packets, k)
    print unfairness
    return

def test():
    #test_list = [ 6, 3, 10, 20, 30, 100, 101, 102]
    #test_list = [ 6, 3, 102, 10, 20, 101, 30, 100]
    #test_list = [ 7, 3, 10, 100, 300, 200, 1000, 20, 30]
    test_list = [ 10, 4, 1, 2, 3, 4, 10, 20, 30, 40, 100, 200]
    #test_list = open('angry_children_input.txt').read().splitlines()     # input.txt - result: 9665150
    main(test_list)

if __name__ == '__main__':
    main()

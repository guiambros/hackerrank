 #!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# --- Cut the Sticks

# You are given N sticks, where each stick is of positive integral length. A
# cut operation is performed on the sticks such that all of them are reduced by
# the length of the smallest stick.
#
# Suppose we have 6 sticks of length
# 5 4 4 2 2 8
#
# then in one cut operation we make a cut of length 2 from each of the 6 sticks.
# For next cut operation 4 sticks are left (of non-zero length), whose length are
# 3 2 2 6
#
# Above step is repeated till no sticks are left.
#
# Given length of N sticks, print the number of sticks that are cut in
# subsequent cut operations.
#
#
# Input Format
# ------------
# The first line contains a single integer N.
#
# The next line contains N integers: a0, a1,...aN-1 separated by space, where ai
# represents the length of ith stick.
#
#
# Output Format
# -------------
# For each operation, print the number of sticks that are cut in separate line.
#
# https://www.hackerrank.com/challenges/cut-the-sticks

#
import sys

DEBUG = True

if (DEBUG): fp=open('input-b.txt')

def print_debug(str):
    if (DEBUG): print "DEBUG: " + str
    return

def read_input():
    if (DEBUG):
        ret=map(int, fp.readline().split(' '))
    else:
        ret=map(int, sys.stdin.readline().split(' '))
    return ret

def read_string():
    if (DEBUG):
        ret=fp.readline()
    else:
        ret=sys.stdin.readline()
    return ret


#@profile
def main():
    n = int(read_input()[0])
    sticks = sorted(read_input())
    while (True):
        num_cuts = sum([1 for x in sticks if x>0])
        if num_cuts==0:
            break
        print num_cuts
        while(sticks.count(0)>0):   # delete zero'ed cells
            sticks.pop(0)
        cut_len = min(sticks)        
        sticks[:] = [s_len-cut_len for s_len in sticks]

# Alternative solution, by Coltin Caverhill (@Coltin)
def solve():
    nSticks = int(read_input()[0])
    stickLengths = sorted(read_input())
    cuts = 0
    totalCutLength = 0
    i = 0
    while i < len(stickLengths):
        print len(stickLengths)-i
        totalCutLength = stickLengths[i]
        while i < len(stickLengths) and stickLengths[i] <= totalCutLength:
            i += 1

if __name__ == '__main__':
    solve()

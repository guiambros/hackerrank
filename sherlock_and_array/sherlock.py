#!/usr/bin/python
#
# Watson gives an array A1,A2...AN to Sherlock. Then he asks him to find if there exists an element in the array,
# such that, the sum of elements on its left is equal to the sum of elements on its right. If there are no elements
# to left/right, then sum is considered to be zero.
#
# Formally, find an i, such that, A1+A2...Ai-1 = Ai+1+Ai+2...AN.
# 
# Input Format 
# The first line contains T, the number of test cases. 
# For each test case, the first line contains N, the number of elements in the array A.
# The second line for each testcase contains N space separated integers, denoting the array A.
# 
# Output Format 
# For each test case, print YES if there exists an element in the array, such that, the sum of
# elements on its left is equal to the sum of elements on its right, else print NO.
# 
# 

import sys

DEBUG = True

if (DEBUG): fp=open('input04.txt')

def print_debug(str):
    if (DEBUG): print "DEBUG: " + str
    return

def read_input():
    if (DEBUG):
        ret=map(int, fp.readline().split(' '))
    else:
        ret=map(int, sys.stdin.readline().split(' '))
        if len(ret)==1: ret=int(ret[0])
    return ret

def main():
    T = read_input()
    T = 10

    for i in range(1, T+1):
        N = read_input()
        A = read_input()
        ret="NO"
        left=right=prev_val=prev_lsum=0
        prev_rsum=sum(A)

        for ptr in range(0, len(A)):
            cur_val = A[ptr]            
            left  = prev_lsum + prev_val
            right = prev_rsum - cur_val

            if left==right:
                ret="YES"
                break
            
            prev_val  = cur_val
            prev_rsum = right
            prev_lsum = left

        #print str(left) + " -- " + str(right) + "    == " + ret
        print ret


if __name__ == '__main__':
    main()

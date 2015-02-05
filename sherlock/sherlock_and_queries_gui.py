 #!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# Watson gives to Sherlock an array: A1,A2,⋯,AN. He also gives to Sherlock two
# other arrays: B1,B2,⋯,BM and C1,C2,⋯,CM.
# 
# Then Watson asks Sherlock to perform the following program:
# 
# for i = 1 to M do
#     for j = 1 to N do
#         if j % B[i] == 0 then
#             A[j] = A[j] * C[i]
#         endif
#     end do
# end do
# 
# Can you help Sherlock and tell him the resulting array A? You should print all
# the array elements modulo (10^9+7).
#
# INPUT
# The first line contains two integer numbers N and M. The next line contains N
# integers, the elements of array A. The next two lines contains M integers
# each, the elements of array B and C.
# 
# OUTPUT
# Print N integers, the elements of array A after performing the program modulo (10^9+7).
# (a+b)%p = ((a%p)+(b%p))%p
#
# https://www.hackerrank.com/challenges/sherlock-and-queries


import sys
from heapq import *

DEBUG = False
LONGINT = 1000000007

if (DEBUG): fp=open('input01.txt')

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
    N, M = read_input()
    A = read_input()
    B = read_input()
    C = read_input()

    # Example:
    #   A=[3,4]
    #   B=[1,1,2]
    #   C=[10,20,30]
    #
    # Naive algo:
    #  i = 1:3
    #    j = 1:2
    #       if j%B[i] then A[j] *= C[i]
    #
    #   i   j  B[i]  C[i]   j%B   A[j*]
    #  -----------------------------------
    #   1   1    1    10     Y    3*10
    #   1   2    1    10     Y    4*20
    #   2   1    1    20     Y    (3*10)*20
    #   2   2    1    20     Y    (4*20)*20
    #   3   1    2    30     -    ==
    #   3   2    2    30     Y    ((4*20)*20)*30
    #
    # Res:  A[1]=(3*10)*20=600  A[2]=((4*20)*20)*30=48000
    #
    
    # Solutions Approach:
    # 1. Pre-calculate a multiplication matrix. Basically a hashtable where each B(i) is unique
    # 2. Put all the elements of the multiplication matrix in a Set
    # 3. Iterate over each element of B, finding the elements of A that need to be multiplied.
    # 
    # More specifically:
    # 
    # Matrix:                                 B[i]
    #   1: 10*20 = 200                   j  |  1      2     3      4      5
    #   2: = 30                         --------------------------------------
    #                                    1  |  MM1
    # Meaning:                           2  |  MM1   MM2
    #   if j is divisible by 1, *200     3  |  MM1         MM3
    #   if divisible by 2, *30           4  |  MM1   MM2          MM4 
    #   if divisible by BOTH, *30*200    5  |  MM1                       MM5
    # 
    # Note that if your matrix multiplication is in ascending order, you just need to go till 
    # j(max). After that you'll never have j%B[i] == 0, and you should break the loop
    # 
    # Items 1 and 2 above are straightforward. But item #3 requires more thinking. In the example
    # above, you have element 2, which gives a multiplier of 30. This means that every A[j] where
    # j is divisible by 2 (2, 4, 6, 8, 10, ...) should be multiplied by 30. Similarly, if we had
    # a third element, we'd say that every A[j] where j = 3, 6, 9, 12, ... should be multiplied by
    # x, and so on. Do you see the pattern?
    # 
    # Basically, we can create a queue, where we apply the multiplier to A[j], and push the next
    # increment back in the queue. For example, for j=2, we multiply A[2] *= 30, and then we 
    # "push back" an operation to multiply also A[4] (and then A[6], A[8] and so on). But once
    # j > N, we can stop, obviously.
    #
    # Now this is easy to implement...

    q = []
    mtx = build_matrix_multiplier(B, C)

    for b, multiplier in mtx.items():
        heappush(q, (b, multiplier, b))

    idx=1
    while len(q)>0:
        idx,mm,inc = heappop(q)
        if idx>N:
            break
        A[idx-1] = (A[idx-1] * mm) % LONGINT
        heappush(q, (idx+inc,mm,inc))
    
    print ' '.join(map(str, A))


def build_matrix_multiplier(B, C):
    ''' Build the matrix of multipliers. For each *unique* elements in B, calculate
        the equivalent multiplier.

        This means that: for every number i where i % B[i] == 0, the multiplier
        is *= C[i]. In other words, suppose you have:
            B = 1, 1, 2, 4, 5
            C = 10, 20, 30, 40, 50

         idx divisible          mutliply A[i]
         by...:                 by:
            1                       x200
            2                       x30
            4                       x40
            5                       x50
    '''
    matrix={}
    for b, c in zip(B, C):
        if b not in matrix:
            matrix[b] = c
        else:
            matrix[b] = (matrix[b]*c) % LONGINT
    return matrix


if __name__ == '__main__':
    main()

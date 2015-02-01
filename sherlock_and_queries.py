 #!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# Watson gives to Sherlock an array: A1,A2,,AN. He also gives to Sherlock two
# other arrays: B1,B2,,BM and C1,C2,,CM.
# 
# Then Watson asks Sherlock to perform the following program:
# 
# for row = 1 to M do
#     for col = 1 to N do
#         if col % B[row] == 0 then
#             A[col] = A[col] * C[row]
#         endif
#     end do
# 
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


from heapq import *
import sys
DEBUG = True
fp=open('sherlock_and_queries_input.txt')

LONGINT = 1000000007

def print_debug(str):
    if (DEBUG): print "DEBUG: " + str
    return

def read_input():
    if (DEBUG):
        ret=map(int, fp.readline().split(' '))
    else:
        ret=map(int, sys.stdin.readlines().split(' '))
    return ret

# ---
#@profile
def main():

    N, M = read_input()
    A = read_input()
    B = read_input()
    C = read_input()

    print_debug("# elements A: %d" % len(A))
    print_debug("# elements B: %d" % len(B))
    print_debug("# elements C: %d" % len(C))
    print_debug("N = %d, M = %d" % (N, M))

    # run!
    mps = {}

    for x, y in zip(B, C):
        if x not in mps:
            mps[x] = y
        else:
            mps[x] = (mps[x] * y) % LONGINT

    q = []

    for k in mps:
        heappush(q, (k, k, mps[k]))

    while len(q) > 0:
        ix, k, y = heappop(q)
        if ix > N:
            break
        A[ix - 1] = (A[ix - 1] * y) % LONGINT
        heappush(q, (ix + k, k, y))

    print ' '.join(map(str, A))
    return

if __name__ == '__main__':
    main()

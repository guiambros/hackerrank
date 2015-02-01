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
<<<<<<< HEAD
# https://www.hackerrank.com/challenges/sherlock-and-queries/
=======
# https://www.hackerrank.com/challenges/sherlock-and-queries
>>>>>>> HEAD@{6}


from heapq import *
import sys
<<<<<<< HEAD
DEBUG = None
=======
DEBUG = True
fp=open('input01.txt')

M = 1000000007
>>>>>>> HEAD@{6}

def print_debug(str):
    if (DEBUG): print "DEBUG: " + str
    return

<<<<<<< HEAD
def read_multiline_input():
    return(sys.stdin.readlines())

class sherlock:
    """A sherlock class"""
    
    #@profile
    def calc_matrix(self, N, M, A, B, C):
        for i in range(0, M):
            for j in range(0, N):
                if ((j+1) % B[i])==0:
                    A[j]=A[j]*C[i]
        return A

    def print_matrix(self, val):
        mod_val=10**9+7
        ret = ''
        for a in val:
            ret=ret + str(a%mod_val) + " "
        print ret.strip()

    #@profile
    def __init__(self):
        self.vars = []

# ---
#@profile
def main(lines=[]):
    # read input
    if (len(lines)==0): lines=read_multiline_input()
    
    # prepare input data
    N, M = map(int, lines[0].split(' '))
    A = map(int, lines[1].split(' '))
    B = map(int, lines[2].split(' '))
    C = map(int, lines[3].split(' '))

    print_debug("N = %d, M = %d" % (N, M))
    print_debug("A = %s" % (A))
    print_debug("B = %s" % (B))
    print_debug("C = %s" % (C))
        
    # run!
    slk = sherlock()
    ret = slk.calc_matrix(N, M, A, B, C)
    slk.print_matrix(ret)
    return

#@profile
def test():
    test_list = open('sherlock_and_queries_input.txt').read().splitlines()     # expected result: 13 754 2769 1508
    main(test_list)
=======
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
            mps[x] = (mps[x] * y) % M

    q = []

    for k in mps:
        heappush(q, (k, k, mps[k]))

    while len(q) > 0:
        ix, k, y = heappop(q)
        if ix > N:
            break
        A[ix - 1] = (A[ix - 1] * y) % M
        heappush(q, (ix + k, k, y))

    print ' '.join(map(str, A))
    return
>>>>>>> HEAD@{6}

if __name__ == '__main__':
    main()

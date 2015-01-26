 #!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# Watson gives to Sherlock an array: A1,A2,,AN. He also gives to Sherlock two
# other arrays: B1,B2,,BM and C1,C2,,CM.
# 
# Then Watson asks Sherlock to perform the following program:
# 
# for i = 1 to M do
#     for j = 1 to N do
#         if j % B[i] == 0 then
#             A[j] = A[j] * C[i]
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

#
# https://www.hackerrank.com/challenges/sherlock-and-queries/


import sys
DEBUG = None

def print_debug(str):
    if (DEBUG): print "DEBUG: " + str
    return

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

if __name__ == '__main__':
    #main()
    test()

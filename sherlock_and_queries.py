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
# https://www.hackerrank.com/challenges/is-fibo


import sys
from numpy import *
DEBUG = True

def print_debug(str):
    if (DEBUG): print "DEBUG: " + str
    return

def read_multiline_input():
    return(sys.stdin.readlines())

class sherlock:
    """A sherlock class"""
    
    #@profile
    def calc_matrix(self, N, M, A, B, C):
        for j in range(0, N, B[i]):
            mult=1
            for i in range(0, M):
                if ((j+1) % B[i])==0:
                    mult = mult*C[i]
            print_debug ("Iteration %d" % j)
            #A = map(lambda x: x*mult, A)

        return A

    def special_case_b_equal_1(self, N, M, A, B, C):
        print_debug("Found special case b=[1,..,1]. Size A: %d" % len(A))
        mult_vec=[]
        
        for i in range(0, M):
            multiplier = C[i]

            newA = map(lambda x: x*multiplier, A)
            A = newA
        print_debug("Size A post-processing: %d" % len(A))
        return A
        

    def print_matrix(self, val):
        mod_val=10**9+7
        ret = ''
        for a in val:
            ret=ret + str(a%mod_val) + " "
        
        ret=ret.strip()        
        print_debug ("Num. lines = %d" % len(ret.split(' ')))
        print_debug ("--Finished!")

    #@profile
    def __init__(self):
        self.vars = []

# ---
#@profile
def main(lines=[]):
    # read input
    if (len(lines)==0): lines=read_multiline_input()
    
    # prepare input data
    print_debug("line 1: %s" % lines[0])

    N, M = map(int, lines[0].split(' '))
    A = map(int, lines[1].split(' '))
    B = map(int, lines[2].split(' '))
    C = map(int, lines[3].split(' '))

    print_debug("# elements A: %d" % len(A))
    print_debug("# elements B: %d" % len(B))
    print_debug("# elements C: %d" % len(C))

    print_debug("N = %d, M = %d" % (N, M))
    #print_debug("A = %s" % (A))
    #print_debug("B = %s" % (B))
    #print_debug("C = %s" % (C))
        
    # run!
    slk = sherlock()
    if (B == M*[1]):
        ret=slk.calc_matrix(N, M, A, B, C)
    else:
        ret=slk.calc_matrix(N, M, A, B, C)

    slk.print_matrix(ret)
    return

#@profile
def test():
    #test_list = open('sherlock_and_queries_input.txt').read().splitlines()     # expected result: 13 754 2769 1508
    test_list = open('input06.txt').read().splitlines()     # expected result: 13 754 2769 1508
    main(test_list)

if __name__ == '__main__':
    #main()
    test()

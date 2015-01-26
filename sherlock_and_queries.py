 #!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# Watson gives to Sherlock an array: A1,A2,⋯,AN. He also gives to Sherlock two
# other arrays: B1,B2,⋯,BM and C1,C2,⋯,CM.
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


import sys
DEBUG = True

def print_debug(str):
    if (DEBUG): print "DEBUG: " + str
    return

def read_multiline_input():
    return(sys.stdin.readlines())

class sherlock:
    """A sherlock class"""
    
    #@profile
    def build_matrix_multiplier(self, row_max, B, C):
        mod_val=10**9+7
        unique_B = set(B)
        matrix_multiplier={}        

        # iterate over all the unique B's, and calculate the total multiplier 
        # for each, using C[row n]*C[row n+1]*C[row n+..]. Store the final
        # matrix in the dict multi_matrix, which will be used later
        for b in unique_B:
            multiplier=1            
            idx=[i for i, x in enumerate(B) if x==b]
            for i in idx:
                multiplier*=C[i]
            
            #for row in range(0,row_max):
            #    if B[row]==b:
            #        multiplier*=C[row]

            matrix_multiplier[b]=(multiplier%mod_val)

        return matrix_multiplier


    #@profile
    def fast_calc_matrix(self, col_max, row_max, A, B, C):
        matrix_multi=self.build_matrix_multiplier(row_max, B, C)
        unique_B = set(B)

        for b in unique_B:


        for col in range (0, col_max):
                if ((col+1)%b)==0:
                    A[col]*=matrix_multi[b]
        return A


    def calc_matrix(self, N, M, A, B, C):
        for i in range(0, M):
            for j in range(0, N):
                if ((j+1) % B[i])==0:
                    A[j]=A[j]*C[i]
        return A

    def print_matrix(self, val):
        ret = ''
        for a in val:
            ret=ret + str(a) + " "
        print ret.strip()
        print_debug ("\n---\n\n")

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

    # run!
    slk = sherlock()

    if (DEBUG):
        ret=slk.fast_calc_matrix(N, M, A[:], B[:], C[:])
        slk.print_matrix(ret)

        ret=slk.calc_matrix(N, M, A[:], B[:], C[:])
        slk.print_matrix(ret)

    else:
        ret=slk.fast_calc_matrix(N, M, A, B, C)
        slk.print_matrix(ret)

    return


def test():
    #test_list = open('sherlock_and_queries_input.txt').read().splitlines()     # expected result: 13 754 2769 1508
    test_list = open('input13.txt').read().splitlines()     # expected result: 13 754 2769 1508
    main(test_list)

if __name__ == '__main__':
    #main()
    test()

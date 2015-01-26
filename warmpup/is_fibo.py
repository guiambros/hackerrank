 #!/usr/bin/python
# -*- coding: UTF-8 -*-

# You are given an integer, N. Write a program to determine if N is an element
# of the Fibonacci Sequence.
#
# The first few elements of fibonacci sequence are 0,1,1,2,3,5,8,13,⋯ A
# fibonacci sequence is one where every element is a sum of the previous two
# elements in the sequence. The first two elements are 0 and 1.
#
#    Formally:
#    fib(0) = 0
#    fib(1) = 1
#     ⋮
#    fib(n) = fib(n-1) + fib(n-2) ∀ n>1
#
# INPUT:
# The first line contains T, number of test cases.
# T lines follows. Each line contains an integer N.
#
# OUTPUT:
# Display IsFibo if N is a fibonacci number and IsNotFibo if it is not a
# fibonacci number. The output for each test case should be displayed in a new
# line.
#
#
# https://www.hackerrank.com/challenges/is-fibo


import sys
DEBUG = None

def print_debug(str):
    if (DEBUG): print "DEBUG: " + str
    return

def read_multiline_input():
    return(sys.stdin.readlines())

class fibonacci:
    """A fibonacci class"""
    fibo_nums=[]

    #@profile
    def build_fibo_matrix(self, highest_num):
        self.fibo_nums.append(0)
        self.fibo_nums.append(1)
        i=2
        while True:
            fib = self.fibo_nums[i-2] + self.fibo_nums[i-1]
            self.fibo_nums.append(fib)
            if (fib>=highest_num):
                break
            i=i+1
            if i>100:   # sanity check, to avoid spinning out of resources
                print "Aborted: number to check too long"
                break
        return

    #@profile
    def print_isfibo(self, array):
        for num in array:
            if num in self.fibo_nums:
                print "IsFibo"
            else:
                print "IsNotFibo"
        return

    def __init__(self):
        self.fibo_nums = []

# ---
#@profile
def main(lines=[]):
    # read input
    if (len(lines)==0): lines=read_multiline_input()
    num_cases = int(lines[0])

    # prepare input data
    array = map(int, lines[1:])   # convert list of strings to int
    print_debug("N = %d, t = %d" % (len(array), num_cases))
    sorted_array = sorted(array)
    
    # run!
    fib = fibonacci()
    fib.build_fibo_matrix(int(sorted_array[-1]))
    fib.print_isfibo(array)
    return

#@profile
def test():
    test_list = open('is_fibo_input.txt').read().splitlines()     # input.txt - result: 9665150
    main(test_list)    

if __name__ == '__main__':
    main()

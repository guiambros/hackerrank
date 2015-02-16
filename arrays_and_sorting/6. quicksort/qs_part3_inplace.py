 #!/usr/bin/python
# -*- coding: UTF-8 -*-
#
import sys

DEBUG = True
a = []

if (DEBUG): fp=open('input3.txt')

def print_debug(str):
    if (DEBUG): print "DEBUG: " + str
    return

def read_input():
    if (DEBUG):
        ret=map(int, fp.readline().split(' '))
    else:
        ret=map(int, sys.stdin.readline().split(' '))
    return ret

def print_array(a):
    print " ".join("%d" % i for i in a)

def main():
    global a
    s = int(read_input()[0])
    a = read_input()
    quicksort_inplace(0, s-1)

def quicksort_inplace(begin, end):
    if (end-begin) < 2:
        return
    pv = a[end]
    left, right = partition_inplace(begin, end)

    l = quicksort_inplace(begin, left)
    r = quicksort_inplace(right, end)
    #ret = a[begin:left] + [pv] + a[left:end]
    #print_array(ret)
    print_array(a)
    return


def quicksort(a):
    if len(a) < 2:
        return a
    pv = a[0]
    left, right = partition(a)

    l = quicksort(left)
    r = quicksort(right)
    ret = l + [pv] + r
    print_array(ret)
    return ret


def partition_inplace(begin, end):
    pv = a[end]
    swapped = []
    ix_largest = 0

    for i in range(begin, end, 1):   # iterave over all elements except last (pivot)
        cur = a[i]

        if cur > a[ix_largest]: # pointer to the largest element known so far
            ix_largest = i

        if (cur < pv) and (i not in swapped):            # swap all elements lower than pivot
            a[i], a[ix_largest] = a[ix_largest], a[i]
            swapped.append(i)
            ix_largest += 1

    a[ix_largest], a[end] = a[end, a[ix_largest] # swap pivot back into the array
    return a[0:ix_largest], a[ix_largest+1:]


def partition(a):
    p = a[0]
    array = a[1:]
    right, left = [], []
    for i in array:
        if i>p:
            right.append(i)
        else:
            left.append(i)
    return(left, right)


if __name__ == '__main__':
    main()

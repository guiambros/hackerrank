 #!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# --- CAVITY MAP
#
# Youa re given a square n×n map. Each cell of the map has a value in it
# denoting the depth of the appropriate area. We will call a cell of the map a
# cavity if and only if this cell is not on the border of the map and each
# cell adjacent to it has strictly smaller depth. Two cells are adjacent if
# they have a common side.
#
# You need to find all the cavities on the map and depict them with character
# uppercase X.
#
#
# Input Format
# 
# The first line contains an integer n (1≤n≤100), denoting the size of the
# map. Each of the following n lines contains n positive digits without
# spaces. A digit (1-9) denotes the depth of the appropriate area.
#
# 
# Output Format
# 
# Output n lines, denoting the resulting map. Each cavity should be replaced
# with character X.
#
# https://www.hackerrank.com/challenges/cavity-map
#

import sys

DEBUG = True

if (DEBUG): fp=open('input10.txt')

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
    n = int(read_string())
    terrain = [[0 for i in range(n)] for i in range(n)]    
    for i in range(n):
        val = read_input()[0]
        terrain[i]=list(str(val))
    out = terrain[:]

    for i in range(1, n-1):
        for j in range(1, n-1):
            depth=terrain[i][j]            
            if depth>terrain[i-1][j] and depth>terrain[i+1][j] and \
               depth>terrain[i][j-1] and depth>terrain[i][j+1]:
                    out[i][j]='X'

    for i in range(n): print "".join(out[i])

if __name__ == '__main__':
    main()

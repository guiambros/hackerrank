# The Utopian tree goes through 2 cycles of growth every year. The first growth
# cycle occurs during the spring, when it doubles in height. The second growth
# cycle occurs during the summer, when its height increases by 1 meter.
# 
# Now, a new Utopian tree sapling is planted at the onset of the spring. Its
# height is 1 meter. Can you find the height of the tree after N growth cycles?
#
# https://www.hackerrank.com/challenges/utopian-tree

def is_odd(n):      
    return (n & 1)

def grow(cycles):
    if is_odd(cycles):
        exp = (cycles+3)/2
        height = 2**exp-2
    else:
        exp = (cycles+2)/2
        height = 2**exp-1
    return height

def main():
    numbers=[]

    t = input()
    for i in range(1, t+1):
        numbers.append(input())

    for cycle in numbers:
        print grow(cycle)

def test():
    for n in range(1, 32):
        print "n = %d   -->  height = %d" % (n, grow(n))
    
if __name__ == '__main__':
    main()


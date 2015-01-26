def flip_bits(n):      
    return ~n + (1<<32)

def main():
    numbers=[]

    t = input()
    for i in range(1, t+1):
        numbers.append(input())

    for n in numbers:
        print flip_bits(n)

def bit_stringify(n):
    return ("00000000000000000000000000000000" + bin(n)[2:])[-32:]

def test():
    x = 1
    print bit_stringify(x)
    print bit_stringify(flip_bits(x))  


if __name__ == '__main__':
    main()


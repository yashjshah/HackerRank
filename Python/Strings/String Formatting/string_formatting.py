from math import log

def print_formatted(number):
    for i in range(1, number+1):
        width = int(log(n,2)+1)
        print("{n:{w}d} {n:{w}o} {n:{w}X} {n:{w}b}".format(n=i, w=width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
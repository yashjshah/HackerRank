if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(int(x) for x in input().split())
    print(hash(integer_list))
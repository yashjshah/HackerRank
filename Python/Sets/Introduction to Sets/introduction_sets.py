def average(array):
    height_set = set(array)
    return sum(height_set)/len(height_set)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
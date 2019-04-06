if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    a = max(arr)
    for x in range(len(arr)-1,-1,-1):
            if arr[x] == a:
                    arr.remove(arr[x])
    print(max(arr))
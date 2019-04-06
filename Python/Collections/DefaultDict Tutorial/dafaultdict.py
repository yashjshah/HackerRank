from collections import defaultdict

A_index = defaultdict(list)
n, m = (int(x) for x in input().split())

for i in range(1, n+1):
    A_index[input()].append(str(i))

for i in range(m):
    b = input()
    if b in A_index:
        print(*A_index[b])
    else:
        print(-1)


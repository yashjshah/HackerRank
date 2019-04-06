from collections import deque

numbers = deque()
for _ in range(int(input())):
    method = input().split()
    if method[0] == "append":
        numbers.append(method[1])
    if method[0] == "pop":
        numbers.pop()
    if method[0] == "appendleft":
        numbers.appendleft(method[1])
    if method[0] == "popleft":
        numbers.popleft()
print(*numbers)

from collections import Counter

_ = input()
shoes = Counter([int(x) for x in input().split()])

income = 0
numCustomers = int(input())
for _ in range(numCustomers):
    size, price = (int(x) for x in input().split())
    left = shoes[size]
    if left:
        income += price
        shoes[size] = left - 1
print(income)

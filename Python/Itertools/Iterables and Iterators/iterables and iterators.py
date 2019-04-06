# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

_ = int(input())
letters = input().split()
k = int(input())

count = 0
combinations = list(combinations(letters, k))
for tup in combinations:
    if 'a' in tup:
        count += 1
print(count/ len(combinations))

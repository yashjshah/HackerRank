# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

line = input().split()
string, r = sorted(line[0]), int(line[1])

combs = list(combinations_with_replacement(string, r))
combs = [''.join(tup) for tup in combs]
print(*combs, sep='\n')


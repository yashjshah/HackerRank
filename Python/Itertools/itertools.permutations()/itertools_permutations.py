# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

line = input().split()
string, r = sorted(line[0]), int(line[1])

permutations = list(permutations(string, r))
permutations = [''.join(tup) for tup in permutations]
print(*permutations, sep='\n')


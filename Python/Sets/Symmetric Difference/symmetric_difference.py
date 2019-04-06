# Enter your code here. Read input from STDIN. Print output to STDOUT

_ = input()
M = {int(x) for x in input().split()}
_ = input()
N = {int(x) for x in input().split()}

print(*sorted(M ^ N), sep = '\n')


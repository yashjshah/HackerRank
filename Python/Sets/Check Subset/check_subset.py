# Enter your code here. Read input from STDIN. Print output to STDOUT

test_cases = int(input())

for _ in range(test_cases):
    _ = int(input())
    A = {int(x) for x in input().split()}
    _ = int(input())
    B = {int(x) for x in input().split()}
    print(A < B)


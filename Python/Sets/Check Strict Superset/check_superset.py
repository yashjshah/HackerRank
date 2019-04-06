# Enter your code here. Read input from STDIN. Print output to STDOUT

A = {int(x) for x in input().split()}

is_A_super = True
test_case = int(input())
for _ in range(test_case):
    B = {int(x) for x in input().split()}
    is_A_super = A > B
    if not is_A_super:
        break
print(is_A_super)


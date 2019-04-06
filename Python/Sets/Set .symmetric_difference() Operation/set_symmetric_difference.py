# Enter your code here. Read input from STDIN. Print output to STDOUT

_ = int(input())
A_numbers = {int(x) for x in input().split()}

_ = int(input())
B_numbers = {int(x) for x in input().split()}

print(len(A_numbers ^ B_numbers))


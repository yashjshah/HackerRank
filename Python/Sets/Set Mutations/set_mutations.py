# Enter your code here. Read input from STDIN. Print output to STDOUT

_ = int(input())
numbers = {int(x) for x in input().split()}

number_commands = int(input())
for _ in range(number_commands):
    command = input().split()[0]
    other_num = {int(x) for x in input().split()}
    if command == 'intersection_update':
        numbers &= other_num
    elif command == 'update':
        numbers |= other_num
    elif command == 'symmetric_difference_update':
        numbers ^= other_num
    elif command == 'difference_update':
        numbers -= other_num

print(sum(numbers))

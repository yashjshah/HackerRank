def parse(result, command, args):
    if command != "print":
        eval("result." + command + "(" + ",".join(args) + ")")
    else:
        print(result)
result = []
n = int(input())
for _ in range(n):
    command = input().split(' ')
    parse(result, command[0], command[1:])


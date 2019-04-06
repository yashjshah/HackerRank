# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    try:
        a,b = (int(x) for x in input().split())
        print(a//b)
    except Exception as e:
        print("Error Code:", e)


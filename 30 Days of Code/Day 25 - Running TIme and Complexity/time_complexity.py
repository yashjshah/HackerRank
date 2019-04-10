def isprime(n):
    if n == 1:
        return 'Not prime'
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            return 'Not prime'
    return 'Prime'

T = int(input())
for i in range(T):
    number = int(input())
    print(isprime(number))
cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    nums = [0,1]
    for i in range(2,n):
        nums.append(nums[i-1]+nums[i-2])
    return nums[:n]
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
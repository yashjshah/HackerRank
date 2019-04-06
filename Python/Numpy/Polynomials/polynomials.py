import numpy

a = list(map(float, input().split()))
b = float(input())

print(numpy.polyval(a,b))
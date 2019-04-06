import numpy

n, m = map(int, input().split())
array1 = numpy.array([input().split() for _ in range(n)], int)
array2 = numpy.array([input().split() for _ in range(n)], int)

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 // array2)
print(array1 % array2)
print(array1 ** array2)
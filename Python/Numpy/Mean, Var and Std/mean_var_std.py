import numpy

numpy.set_printoptions(legacy = '1.13')
n, m = map(int, input().split())
array = numpy.array([input().split() for _ in range(n)], int)

print(numpy.mean(array, axis = 1))
print(numpy.var(array, axis = 0))
print(numpy.std(array, axis = None))
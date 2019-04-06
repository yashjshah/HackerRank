import numpy

numbers = tuple(map(int, input().split()))
print(numpy.zeros(numbers, dtype = numpy.int))
print(numpy.ones(numbers, dtype = numpy.int))


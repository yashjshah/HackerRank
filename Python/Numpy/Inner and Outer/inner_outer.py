import numpy
 
array1 = numpy.array(input().split(), int)
array2 = numpy.array(input().split(), int)

print(numpy.inner(array1, array2))
print(numpy.outer(array1, array2))
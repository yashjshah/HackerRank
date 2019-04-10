#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
count = 0
is_sorted=False

while not is_sorted:
    is_sorted = True
    for i in range(0,len(a)):
        if i<len(a)-1:
            if a[i]>a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
                is_sorted=False
                count +=1
print('Array is sorted in {} swaps.'.format(count))
print('First Element: {}'.format(a[0]))
print('Last Element: {}'.format(a[len(a)-1]))



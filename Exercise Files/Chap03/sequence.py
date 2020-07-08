#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = [ 1, 2, 3, 4, 5 ]

# changing i in spot 2
x[2] = 52

for i in x:
    print('i is {}'.format(i))

# can also use RANGE(start, end, step by)
y = range(12)

print(y)

# could change this to a list using a list contstructor
l = list(range(10))

print(l)

# Can use a Dictionary like this

a = True

print(a)

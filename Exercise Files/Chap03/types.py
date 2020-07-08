#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 7
y = 70.00

print('x is {}'.format(x))

# f strings are used in 3.6 and >
# they do the same thing, they use the Format Method
print(f'x is {x}')



print('y is a: ', type(y))

print(type(x))

print('weird Tuple stuff')

a = (1, 'two', 3.0, [4, 'four'], 5)
b = (1, 'two', 3.0, [4, 'four'], 5)
print(f'x is {a}')

print(type(a))
print(id(b)) # id(object) Returns an Unique ID for given object


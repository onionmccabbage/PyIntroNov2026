# mathematical operators
# + - / *  
# also ** (raise to the power)
# // means floor division
a = 3
b = 10
print( b//a ) # 3
# also we have % which is used for 'modulo' or remainder
print(b%a) # 1

# using a generator
# we may need to carry out some operation across a very large quantity of values
# e.g. we may need the squares of a series of numbers
r = range(0, 10**5)
print( r )
# NB a generator is like a range, in that only the generator exists in memory
# all the generated values are only provided as needed
# in this way a generator is an efficient object
g = (i**2 for i in range(0, 10, -1)) # this is a generator object
print(g) # here we see that this is a generator obj
x = 9 # 9 is 3**2
if x in g:
    print('it is a square number')

# we may choose to iterate over our generator
# we can use for... for iterate over any ordinal collection
# that is list, tuple, string, range, generator
for _ in g:
    print(_, end=', ')
# careful - the generator has now been exhausted
print('.............................')
for _ in g:
    print('value')
# alternative:
# for _ in r:
#     print(_**2)

# we may need to reuse a generator repeatedly
f = (i**0.5 for i in range(1,10))
f_inst1 = f
f_inst2 = f # these all refer to the same object
for _ in f_inst1:
    print(_)
print('.................')
# we have already exhausted the generator, so every instance is also exhausted
for _ in f_inst2:
    print(_)
print('.................')

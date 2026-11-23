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
# NB a generator is like a range, in that only the generator exists in memory
# all the generated values are only provided as needed
# in this way a generator is an efficient object
g = (i**2 for i in r) # this is a generator object
print(g)
x = 9 # 9 is 3**2
if x in g:
    print('it is a square number')
# in python 'comprehension' means to comprehensively 
# deal with every member of a collection

# here is a range
r = range(-97, 97, 7) # start, stop-before, step=1

# here is a generator we must use ()
g = ( i%3 for i in r ) # here only the generator object exists in memory
# we may iterate over the generator
for _ in g:
    print(_)

# list comprehension. We must use []
# What we do is use a generator to populate a list
lc = [ i%3 for i in r ] # here all the generatted values exists in memory
print(lc)
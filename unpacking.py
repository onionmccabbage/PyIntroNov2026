# we may populate several values at one time

test_results = (True, False, True, True, True, False) # tuple cannot be altered

# we have an implicit tuple
rA, rB, rC, rD, rE, rF = test_results # each member of the collectin gets assigned to a variable

print( rA, rB, rC, rD, rE, rF ) 

# a one member tuple
a = (3) # not a tuple
b = (3,) # this is a tuple containing a single value
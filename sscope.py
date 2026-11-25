# Python responect global and local scopes

# here is a global scope object

g = {'n':'worldwide', 'v':234}

def fnZ():
    '''every function will have its own local scope'''
    global g # we now bring teh global object in to this code block
    g = 'this is within the scope of the function'
    print(g)

fnZ()
print(g)
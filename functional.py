# we may choose to write our code within functions

def fnB():
    print('funcion B')

def fnA():
    fnB()
    print('function A')

fnA()

# the advantages of writing functions
# - encapsulate functionality within a function
# - we may re-use that function by calling it whenever we need it
# - we may import or function into other modules
# - we can unit test functions
# - several people can work across a project, each responsible for functions

# we may choose to write our code within functions

def fnB():
    print('funcion B')

def fnA():
    fnB()
    print('function A')

# we may choose to accept function arguments
def fnC(n=1): # can choose default if we need
    pass

def fnD(*args):
    '''all the arguments provided to this function 
    will be gathered into a tuple called args'''
    # we typically use if to act differently depending on how many arguments
    for _ in args:
        print(_)

def fnE(**kwargs):
    '''any keyword arguments will be gathered into a dict called kwargs'''
    print(kwargs, type(kwargs))


if __name__ == '__main__':
    fnA()
    # explore the tuple of arguments
    fnD() # no arguments
    fnD(1) # 
    fnD(4,2) # no arguments
    fnD(True, None, [], {}) # 
    # using the kwargs
    fnE(n=1)
    fnE(m=False, n=1)
    fnE(n=1, q=(1,))
    fnE(n=1, l = [1,2,3,4,5], h={4,3,7,7,7,2,1})


    # the advantages of writing functions
    # - encapsulate functionality within a function
    # - we may re-use that function by calling it whenever we need it
    # - we may import or function into other modules
    # - we can unit test functions
    # - several people can work across a project, each responsible for functions

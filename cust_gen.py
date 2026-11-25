# we may choose to write a generator of our own

def getNextValue():
    '''this function will behave a a generator, yielding useful values on demand'''
    start = 3
    stop = 11
    while True:
        yield start # yield makes a normal function into a generator
        start += 1
        if start >= stop:
            break # cease the while loop

if __name__ == '__main__':
    g = getNextValue() # we have an instance of our generator
    for _ in g:
        print(_)
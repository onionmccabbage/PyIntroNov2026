# higher order functions let us pass function objects as the 
# arguments to another function

def mult(m):
    '''simple multiply m by three'''
    return m*3

def makeInitialCap(s):
    return s.capitalize()

if __name__ == '__main__':
    # we can use map to apply any function to every member of a collection
    c = (4,5,6,7,8) # any iterable collection may be used
    c3 = list( map(mult, c) )
    print(c3) # list derived from a map object

    words = 'this is a sentence with many lower cae words'
    wCap = list ( map( makeInitialCap, words ) )
    print( wCap )

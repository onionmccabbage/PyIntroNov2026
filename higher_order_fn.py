# higher order functions let us pass function objects as the 
# arguments to another function

def mult(m):
    '''simple multiply m by three'''
    return m*3

def makeInitialCap(s):
    return s.capitalize()

# as well as map we may use filter
# filter will use a function to find True or False outcome
# then the results will either be included or excluded fom the filter
# 
def longWordsOnly(l):
    '''return True if l is more than five letters
    Otherwise return False'''
    if len(l)>5:
        return True
    else:
        return False

if __name__ == '__main__':
    # we can use map to apply any function to every member of a collection
    c = (4,5,6,7,8) # any iterable collection may be used
    c3 = list( map(mult, c) )
    print(c3) # list derived from a map object

    words = 'this is an extremely vague sentence containing many lower-case words'
    wCap = list ( map( makeInitialCap, words ) )
    print( wCap )

    wordList = ['long', 'extremely', 'pythonic', 'Ericsson', 'Genoa']

    # make use of the filter function
    longs = list( filter( longWordsOnly, wordList ) )
    print( longs )


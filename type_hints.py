# Recent version of Python allow for type hints

# be careful: type hints are useful to remind us what we expect from a return of a function
# but Python will never take any notice of the type hinting
# Some development tools//IDEs will enforce typing so you cannot run code until it is correct
def fn()->bool:
    '''this function includes type hints'''
    return [4,3,2,1]

def fnB(a:str, b:bool, c:set)->None:
    ''' we expect this function to return None (i.e. nothing of any interest to us)'''
    return (4,)

if __name__ == '__main__':
    print( fn() )
    print( fnB(True, (1,), 'hahahahaaahaahhhaahhaaa' ) )
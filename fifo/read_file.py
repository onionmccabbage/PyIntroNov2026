# we may also read back from a file

def readFromFile():
    '''retrieve the contents of a text file'''
    fin = open('logsGoHere/output.txt') # 'rt' is the default
    with fin:
        retrieved = fin.read() # read will retrieve the entire file into one string
        # when the 'with' clause ends, the file access object will be released
    return retrieved

def readLinesFromFile():
    '''retrieve all the text into a list of strings'''
    fin = open('logsGoHere/output.txt', 'rt') 
    with fin:
        lines = fin.readlines() # this always retrieves each line into a string within a list
    return lines

if __name__ == '__main__':
    r = readFromFile()
    print(r, type(r))
    l = readLinesFromFile()
    print(l, type(l))
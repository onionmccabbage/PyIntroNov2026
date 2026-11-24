# we may choose to print to a text file

def printToFile(m):
    '''print the incoming object 'm' to a text file'''
    # we need a file acccess object
    fao = open('logsGoHere/output.txt', 'at') # 'at' will append text (or create the file if it doesnt exist)
    # by default the print statement will always add a new line character to the end
    print(m, file=fao) # instead of printing as usual, this will print to a text file
    # remember to tidy up
    fao.close() # this releases the file access object so resources are available

if __name__ == '__main__':
    '''exercise the current module'''
    words = 'this is an important report'
    printToFile(words)




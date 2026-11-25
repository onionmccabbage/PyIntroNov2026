# here we write text into a persistent file

def writeToFile(m):
    '''persist the incoming object 'm' to a text file '''
    try:
        fout = open('logsGoHere/output.txt', 'a') # 't' is the default
        with fout:
            # when we use 'write' there is no default new-line character
            # fout.write(m)
            # fout.write('\n') # we choose when to terminate the line
            fout.write(f'{m}\n') # minimize the write operations for performance
            # when we use the 'with' operator, it will automatically close the asset when done
    except Exception as err:
        print(err) # we may choose to log it to a file
if __name__ == '__main__':
    t = 'words to be logged to a file'
    writeToFile(t)

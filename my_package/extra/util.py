# this module may contain utilities we need elsewhere

# we do not have to proivide arguments into a functino
# but we may choose to pass in arguments
def cleanUpStringToNumber(s):
    '''this function will check that we have a string
    then convert it to a numeric integer value'''
    if type(s) == str: # str is always a string
        # result = int(float(s)) # here I choose to make an int
        # return result
        return int(float(s)) # we may chooseto write it all on one line

# any code which is not indented is run whenever the module is executed

# if __name__ == '__main__':
# Any module which we run directly is given the name '__main__'
print( __name__ ) # what does Python call this module
# exercise this module by calling our function
d = '3.147'  # we have a string
n = cleanUpStringToNumber(d) # we pass the string into our function
print(d, n, type(d), type(n))
# what if we have a non-number....
e = 'junk'
    
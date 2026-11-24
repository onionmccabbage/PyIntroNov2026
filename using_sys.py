# there is a built in library called sys
import sys
# this gives us access to the system in which Python is running
print(sys.platform)
# we can make use of sys to grab any incoming system argument variables
print(sys.argv) # this is always a list
print(sys.argv[0]) # [0] is always the name of the current module
# we often check to see if additional system arguemnts have been provided
if len(sys.argv) > 1:
    print( '-'.join( sys.argv[1:] ) )
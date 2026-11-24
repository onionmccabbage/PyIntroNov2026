# we will use the requests library to retrieve specofoc 'todos' from a REST API
import requests
import sys

#NB we may choose to put our validation logic into a separate module (and import it here)
def validate(n=1): # we may provide a default for the arguments
    '''ensure the incoming value is a positive integer'''
    if type(n) == int and n>0:
        return n
    else:
        # we could choose to raise an exception
        return 1 # an option is to provide a sensible default

def getTodo(t):
    '''retrieve the todo with id 't' from REST API'''
    clean = validate(t) # this value will over-write the default n=1
    try:
        td = requests.get(f'https://jsonplaceholder.typicode.com/todos/{clean}')
        # td_structure = td.json() # here we retrieve just the JSON as Python data structures
        return td # here we choose to return the entire response object
    # we may choose to handle different types of exception
    except ConnectionError as ce:
        print(f'Problem connecting: {ce}')
    except Exception as err:
        print(f'Something went wrong: {err}')
    finally:
        print('the finally block is optional. It will always run, even if thiere is no exception')

def main():
    '''run the main stuff'''
    # first we check to see if there are additional system argument variables
    if len(sys.argv)>1:
        # CAREFUL: sys.argv are ALWAYS string
        r = int(float( sys.argv[1] )) # try to convert the incoming sting to a number
    else:
        r = 1 # a sensible default
    # additional system arguments
    if len(sys.argv)>2: # always check that there is actually a member to be had!!
        print( sys.argv[2], type(sys.argv[2]) )
    
    c = getTodo(r) # pass in a value
    print(c, type(c), c.json())

if __name__ == '__main__':
    main()
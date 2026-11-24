# we will use the requests library to retrieve specofoc 'todos' from a REST API
import requests

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
        td_structure = td.json() # here we retrieve just the JSON as Python data structures
        return td_structure
    except Exception as err:
        print(f'Something went wrong: {err}')

def main():
    '''run the main stuff'''
    c = getTodo(4) # pass in a value
    print(c, type(c))

if __name__ == '__main__':
    main()
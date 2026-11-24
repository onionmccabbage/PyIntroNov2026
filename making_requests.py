# we need to pip install the requests library
import requests

def getData():
    '''this function will use the requests library to grab data from the internet
    We call this API access, often using REST'''
    api_url = 'https://jsonplaceholder.typicode.com/users'
    # use the reursts library to get some external data
    # we may also use get post put update delete
    # in addition we can access the request, the headers etc.
    r = requests.get(api_url)
    # we just want the JSON 
    data = r.json() # this also converts the JSON text into Python structures
    return data

def getOnePhoto(n):
    '''retrieve the data relating to a single photo, id passed in as 'n' '''
    api_url_root = 'https://jsonplaceholder.typicode.com'
    category = 'photos'
    # we should validate that n is a positive integer
    if type(n)==int and n>0:
        # we REpresent the STate in the URL
        url = f'{api_url_root}/{category}/{n}'
        photo = requests.get(url)
        return photo.json() # we are only interested in the JSON data
    else:
        raise TypeError('n must be a positive integer')

if __name__ == '__main__':
    users = getData()
    print(users, type(users))
    # we now have a list of dict objects
    for i in users:
        print( i, type(i))

    # grab just one piece from the data structure
    print( users[0]['name'] ) # we use indexing (or slicing) to parse our data

    print( users[4]['address']['city'], users[4]['name'] )

    # if we need several users....
    print( users[3:6] )

    # call one photo function
    try:
        p = getOnePhoto('42')
        print(p, type(p))
    except TypeError as te:
        print(te)

    # sometimes we have a large data collection and we need to handle
    # each member individually
    (u1, u2, u3) = users[0:3]# here we unpack the first few members
    print( u1['name'], u2['name'], u3['name'] )
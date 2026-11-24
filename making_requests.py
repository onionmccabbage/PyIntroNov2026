# we need to pip install the requests library
import requests

def getData():
    '''this function will use the requests library to grab data from the internet
    We call this API access, often using REST'''
    api_url = 'https://jsonplaceholder.typicode.com/users'
    # use the reursts library to get some external data
    r = requests.get(api_url)
    # we just want the JSON 
    data = r.json() # this also converts the JSON text into Python structures
    return data

if __name__ == '__main__':
    users = getData()
    print(users, type(users))
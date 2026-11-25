# notice the name of the file has no relationship to any class names

class Person:
    '''Person will have name, age and auth'''
    # we may restrict which proeprties we are permitting
    __slots__ = ['__name', '__age', '__auth']
    def __init__(self, n, a, auth): # the __init__ is called once only, when we create an instance
        self.name = n
        self.age  = a
        self.auth = auth
    # by default all the properties are directly accessible
    # we may choose to write getter and setter methods for our properties
    @property
    def name(self): # this will be called whenever an instance tries to access the 'name' proeprty
        return self.__name
    @name.setter
    def name(self, new_n):
        if type(new_n) == str and new_n != '':
            self.__name = new_n
        else:
            raise TypeError(f'{new_n} is not valid (must be a non empty string)')
    # get/set methods for age (a positive integer)
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, new_a):
        if type(new_a)==int and new_a >0:
            self.__age = new_a
        else:
            self.__age = 42 # here we simply set a sensible default
    # and again for auth (permit 'admin' 'exec' and 'user')
    @property
    def auth(self):
        return self.__auth
    @auth.setter
    def auth(self, new_auth):
        if new_auth in ('admin', 'exec', 'user'):
            self.__auth = new_auth
        else:
            self.__auth = 'user' # we could raise an exception
    # we may add further methods for our class
    def birthday(self):
        '''increment the age by one'''
        self.__age += 1
    # we may choose to control how class instances will be printed
    def __str__(self):
        return f'{self.name} is {self.age} and has {self.auth} rights'

if __name__ == '__main__':
    ''' exercise this module '''
    # we may create as many instancs as we wish
    oenid = Person('Oenid', 44, 'admin') # the __init__will be called here
    ethel = Person('Ethel', 32, 'exec')
    june  = Person('June', 46, 'user')
    oenid.age = None # we mutate a property - calls the setter (might result in a default)
    oenid.birthday() # this calls the method
    print(oenid.name, oenid.age)
    print( type(oenid) )
    # __slots__ prevents any additional arbitrary mangled properties
    # oenid.__oops = 'this will fail'
    # what happens if we print an instance
    print( ethel )
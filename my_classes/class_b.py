# notice the name of the file has no relationship to any class names

class Person:
    '''Person will have name, age and auth'''
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

if __name__ == '__main__':
    ''' exercise this module '''
    # we may create as many instancs as we wish
    oenid = Person('Oenid', 42, 'admin') # the __init__will be called here
    ethel = Person('Ethel', 32, 'exec')
    june  = Person('June', 46, 'user')
    # oenid.age = None # we mutate a property
    print(oenid.name, oenid.age)

    print( type(oenid) )
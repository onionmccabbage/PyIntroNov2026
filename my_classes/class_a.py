
class Auto:
    # we often choose to write an initializer for our class
    # the __init__ is only called ONCE (when we make an instance)
    def __init__(self, name, needs, timeout): # 'self' refers the this class
        self.name = name # this will call the name setter decorated function
        self.needs= needs # we assign the incoming parameters to 'self'
        self.timeout = timeout # this calls the decorated setter for timeout
    # we need a reliable mechanism to validate both on creation and mutation
    @property # decorator
    def name(self): # this is the property getter
        # a property will be mangled if we use two underscores like this
        return self.__name # mangling, so this value is not available outside the class
    @name.setter  # NB if we choose to NOT write a setter the nwe have a read-only property
    def name(self, new_name): # this is the property setter
        if type(new_name)==str and len(new_name)>0:
            self.__name = new_name
        else:
            raise TypeError('Name must be a string')
    # we need get/set methods for 'timeout'
    @property
    def timeout(self):
        return self.__timeout
    @timeout.setter
    def timeout(self, new_t):
        '''here we can validate: timeout must be a positive int or float'''
        if type(new_t) in (int, float) and new_t>0:
            self.__timeout = new_t
        else:
            raise TypeError('timeout must be a positive number') 
    # NB every class method must take 'self' as the first argument
    def appendNeed (self, new_need):
        self.needs.append(new_need)

if __name__ == '__main__':
    '''we may create instances of our class'''
    auto1 = Auto('dev', ['Python',], 30) # when we make an instance, the __init__ is called once
    auto2 = Auto('prod', ['Python',], 10)
    auto1.name = 'development' # this calls the name setter method
    auto1.appendNeed('code')
    # examine our class instances
    print( auto1.name, auto1.needs ) # here we call the getter for each property
    print( auto2.name )

    # check to see our 'timeout' validation operates as expected
    try: # if we write 'try' we are obliged to also write 'except'
        auto1.name = False # fail
        auto1.timeout = -88 # fail
    except TypeError as te:
        print(te)

class Auto:
    # we often choose to write an initializer for our class
    def __init__(self, name, needs): # 'self' refers the this class
        self.name = name # this will call the name setter decorated function
        self.needs= needs # we assign the incoming parameters to 'self'
    # we need a reliable mechanism to validate both on creation and mutation
    @property # decorator
    def name(self):
        return self.__name # mangling, so this value is not available outside the class
    @name.setter
    def name(self, new_name):
        if type(new_name)==str and len(new_name)>0:
            self.__name = new_name
    
    
    
    # NB every class method must take 'self' as the first argument
    def appendNeed (self, new_need):
        self.needs.append(new_need)

if __name__ == '__main__':
    '''we may reate instances of our class'''
    auto1 = Auto('dev', ['Python',]) # when we make an instance, the __init__ is called once
    auto2 = Auto('prod', ['Python',])
    auto1.name = 'development'
    auto1.appendNeed('code')
    # examine our class instances
    print( auto1.needs )
    print( auto2.name )
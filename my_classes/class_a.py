
class Auto:
    # we often choose to write an initializer for our class
    def __init__(self, name, needs): # 'self' refers the this class
        self.name = name
        self.needs= needs # we assign the incoming parameters to 'self'
    # NB every class method must take 'self' as the first argument
    def appendNeed (self, new_need):
        self.needs.append(new_need)

if __name__ == '__main__':
    '''we may reate instances of our class'''
    auto1 = Auto('dev', ['Python',]) # when we make an instane, the __init__ is called once
    auto2 = Auto('prod', ['Python',])
    auto1.appendNeed('code')
    # examine our class instances
    print( auto1.needs )
    print( auto2.name )
from class_b import Person
# we use classes to encapsulate properties, methods and validation
# we may then inherit into a new class

class Customer(Person):
    '''inherit all the features of a the Person class'''
    def __init__(self, n, a, auth, company):
        super().__init__(n, a, auth)
        self.company = company

if __name__ == '__main__':
    customerA = Customer('Floella', 63, 'user', 'Neueda')
    print(customerA)
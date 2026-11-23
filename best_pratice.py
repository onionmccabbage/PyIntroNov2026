# when asking for inout we may attempt to cast directly to a numeric value
q = int( float ( input('Please enter  number: ') ) )
print(q, type(q))

# when would we choose to use a particular data type?
# for collections to use minimal memory space, choose a tuple
# ... but if you may need to change it at runtime
# i.e. mutate, then use a list
# ie is latin for 'id est' which in english means 'that is...'
# the advantage of list/tuple is they are ordinal (makes them easy to iterate)
# However, if the order is irrelevant, it may suit your purpose to choose a dict
# then we may associate keys with the data members
# so, choose a dict, when we need association rather than index by number
# e.g. (which means 'for example')
person = {'fn':'Floella', 'ln':'Benjamin', 'age':82}
# A set would be used when we need to ensure unique values
# so a quality of service monitor (QoS) may need to check just unique items
items = {'temperature', 'humidity', 'wind-speed', 'dropped-packets'}
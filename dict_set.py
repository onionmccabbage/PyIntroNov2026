# NB strings may be declared using single quote, double quote, triple quoe or triple dounle wuote
s1 = 'single quotes'
s2 = "double quotes"
s3 = '''tripple quotes
allows new lines etc within the quotes'''
s4 = """tripple double quotes also permit new lines within the sting
like this"""
# N.B. is a short acronum for 'nota bene' 
# which is latin for 'take note'

# A dictionary is a non-ordinal collection of key:value pairs of any data type
w = {"target":'docker',
     'resources':('Python', 'db', 'security'),
     'success':True
    }

# we can still use slicing
print(w, type(w), w['resources'], w['resources'][1])
# dict is always mutable
w['oobly']='additional'
w['check']=[5,4,3,2,1]
w['success'] = False


# we may iterate over a dict
for (k, v) in w.items():
    if type(v) in (list, tuple):
        for _ in v:
            print('\t', _) # \t will print a tab
    print(k, v)

# since a dict can contain any data type, we may have ordinal members
# we can accces these using slicing
print(  w['check'][2:4]  ) # 3,2

# we may define function and if we choose, we may write a 'docstring'
def fn():
    '''this is  docstring where we may choose to write info about 
    this function'''

# now, what about sets....
# a set is a unique collection of data members
# a set is not ordinal but is mutable
r = {4,5,6,7,3,4,8} # just entries (no keys)
r.add(3)
r.add('four')
r.add(None)
r.add(0)
r.add(False)
r.remove(8)
print(r, type(r))
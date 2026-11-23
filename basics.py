# Here is a comment
a = 1   # integer
b = 7.3 # floating point number

print(a, b)
print( type(a), type(b) )

# Python has several simple data types
# int, float, bool
# 
# Also there are some collection data types
# a string is an imutable ordinal collection of characters 
s = 'hello this is a text sting containing words'

# we may use indexing and slicing to access members of an ordinal collection
print( s[0] ) # h
print( s[0:12] ) # [start:stop-before]
# mini challenge: how could we extract the word 'text' from this string?
print( s[16:20] )

# working with strings: .upper() .lower() .title() .capitalize()
S = s.capitalize() # NB Python is case-sensitive
print(S)

# other ordinal collections: list and tuple
l = list(  (1,2,3,4,5)  )
k = [5,4,3,2,1] # lists are mutable
k[4] = 99
# append will place the new member at the end of the collection (with a new index )
k.append('hello') # also .pop() will remove just the last member
k.append(2)
k.insert(3, True) # the other members shift along
print(k, type(k), l, type(l))
print(k)
# if we remove 1, it removes True
k.remove(True) # the value 'True' evaluates to 1
# the value False evaluates to 0
k.remove(2) # finds the first occurence of the actual value to be removed
print(k)

# tuple: immutable ordinal collection of any data type
f = tuple( (4,3,8,2,9) )
g = (4,2,9,-4,31,45)
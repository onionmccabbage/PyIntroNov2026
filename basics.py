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
j = 'hello'
k = 32
l = 66.5

s = (j, k, l)

# we may use 'for' to iterate over any ordinal collection
for i in s:
    if type(i) in (int, float):
        print('number')
    else:
        print('not a number')

# we may use a range object
# range is efficient: we may gra as many values as we need
# but only the rangel object eists in memory
# NB ** will raise to the power...
# by the way, the 'step' may be negative in any iteration
r = range(-10**4, 10**4, 2) # range(start, stop-before, step=1)
for _ in r:
    print(_)

print(type(r))

# demo (no need to write this)
# d = 'dkfjel ahefkg ehrfi uRVAH RLUVK DF.K\Saskvdkrvdkfjvz,dfv,zsdfbz,hvfzjhsdv'
# for _ in d:
#     print(_, end=(', ')) # by default print adds a new line, but we may override

x = 0
while True:
    print('hello')
    x += 1 # we may increment like this. Also -= and *=
    if x == 8:
        break # this will break out of any kind of loop

# logic
#we may ask the user to enter a value
# be careful this ALWAYS returns a string value
w = input('please enter a value: ')
print(type(w))
# we may check if we have a numeric value like this:
if w.isnumeric(): # isnumeric means the string only contains digits
    # then we could cast the string to a number
    x = int(w) # try to make w into an integer
    print(x, type(x))

# we may cast any number to a float
q = -999
p = float(q) # we now have a floating point value

if w == 'quit':
    print('bye')
elif w=='lunch': # we may have several elif statements (or none)
    print('time to break')
else:
    print('done')

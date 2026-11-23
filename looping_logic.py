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


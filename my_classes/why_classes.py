# Python hs many built in classes already
# we may retain information within numbers, collections
# we may also write functions to carry out operations
# here is a dummy automation proposal
autoProcess = {
    'auto' : 'process',
    'needs': ('Python', 'code', 'data', 'docker'),
    'steps' : {'assemble', 'unit test', '', 'deploy'}
}
# there is still no easy eay tp enforce validation

# A class will let us:
# - collect related data as class properties
# - write related functions (e.g. validation) as class methods
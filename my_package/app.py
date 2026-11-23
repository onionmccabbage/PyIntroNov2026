# we often call our main module 'app' or 'main' or sometimes 'index'
# We can import from relative locations
# we may also import from absolute locations
# e.g. c:\inhere\keepgong\thisfile


# we may need to import from another module
# if we importfrom a package then we use dot notation
# a package is simply a folder
from extra.util import cleanUpStringToNumber
# be careful - when you import ALL THE CODE RUNS!!!!


# anything we import is then available within this module

# if __name__ == '__main__':
x = '44.2'
print( cleanUpStringToNumber( x ) )
# if we run this module directly, then python will name it '__main__'
print( __name__ ) # what does Python call this module

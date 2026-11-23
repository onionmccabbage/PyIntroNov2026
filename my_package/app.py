# we often call our main module 'app' or 'main' or sometimes 'index'
# We can import from relative locations
# we may also import from absolute locations
# e.g. c:\inhere\keepgong\thisfile


# we may need to import from another module
# if we importfrom a package then we use dot notation
# a package is simply a folder
from extra.util import cleanUpStringToNumber

# anything we import is then available within this module


x = '44.2'

print( cleanUpStringToNumber( x ) )


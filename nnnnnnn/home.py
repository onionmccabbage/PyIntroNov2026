from more import simple
# anything that is imported is given a specific name

# predefined: the module we directly execute is given a predefined name by Python
# the name that python gives is always __main__ when we run a module directly
print(f'Python calls this module {__name__}')

# we use this feature to check if we running the module
if __name__ == '__main__':
    print(simple())
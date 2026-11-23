def simple():
    return 'hello from more simple'

def simple1():
    return ' more simple stuff'

print(f'Python calls this module {__name__}')

# there are no 'entry points' in Python
if __name__ == '__main__':
    # then we choose to exercise this module
    print(f' directly {simple()}')
    print(f' directly {simple1()}')
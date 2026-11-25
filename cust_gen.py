# we may choose to write a generator of our own
from datetime import datetime
import time

def getNextValue():
    '''this function will behave a a generator, yielding useful values on demand'''
    start = 3
    stop = 11
    while True:
        # as soon as we use 'return' the function must cease
        yield start # yield makes a normal function into a generator
        start += 1
        if start >= stop:
            # if we choose to include a return then the yield will be overriden and the generator will cease
            return 'done' # cease the while loop

# this kind of generator is very useful. We may use it when writing log file
# so we can add a datetime stamp to persistent records
def genTimestamp():
    '''This custom generator will yield a date-time picture whenever we need one'''
    while True: # careful -this will never end! (unless we kill the running program)
        now = datetime.now() #get the date and time according to the current machine clock
        dt_str = now.strftime('%d/%m/%y %H:%M:%S')
        yield dt_str

if __name__ == '__main__':
    g = getNextValue() # we have an instance of our generator
    for _ in g:
        print(_)
    # we need an instance of our generator
    dtg = genTimestamp()
    # it is possible to grab just the next available member from any generator
    n = dtg.__next__()
    print(n)
    time.sleep(5)
    m = dtg.__next__()
    print(m)
    time.sleep(5)
    p = dtg.__next__()
    print(p)
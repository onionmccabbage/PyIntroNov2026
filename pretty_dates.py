# import datetime # the entire datetime package
# alternative
from datetime import datetime # just the datetime module from the datetime package

def showTodaysDate():
    '''return a nicely formatted representation of the date and time
    according to the current computer'''
    # why datetime.datetime....?
    # return datetime.datetime.now() # if we import datetime
    # use strftime to make a 'picture' of the date
    dt = datetime.now().strftime('%d-%m-%y %H:%M:%S')
    return dt
    # return datetime.now()

if __name__ == '__main__':
    d = showTodaysDate()

    print(d)



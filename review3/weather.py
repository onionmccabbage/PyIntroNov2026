class Weather():
    '''
    The Weather class takes a string for the city and description
    and a floating point number or integer for the temperature
    '''
    # NB slots should always begin with __
    __slots__ = ['__city','__desc', '__temp']
    def __init__(self, city, desc, temp):
        self.city = city # this will call the city setter method
        self.desc = desc
        self.temp = temp
    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, new_city):
        if type(new_city) == str and len(new_city)>2:
            self.__city = new_city # name-mangling so there is no aces to this outside the class
        else:
            self.__city = 'Athlone'
    @property
    def desc(self):
        return self.__desc
    @desc.setter
    def desc(self, new_desc):
        if type(new_desc) == str:
            self.__desc = new_desc
        else:
            self.__desc = '' # default to an empty string
    @property
    def temp(self):
        return self.__temp
    @temp.setter
    def temp(self, new_temp):
        if type(new_temp) in (int, float):
            self.__temp = new_temp
        else:
            self.__temp = 12 # a reasonable default
    def __str__(self):
        match self.__temp:
            case t if t <=0:
                feels = 'freezing'
            case t if 0<t<=12:
                feels = 'chilly'
            case t if 12<t<=22:
                feels = 'warm'
            case t if 22<t<=28:
                feels = 'hot'
            case _: # _ will match all remaining values
                feels = 'baking'
        # alternatively
        # if self.temp <=0:
        #     feels = 'freezing'
        # elif 0 < self.temp <=12:
        #     feels = 'chilly'
        # elif 12 < self.temp <=24:
        #     feels = 'warm'
        # elif 24 < self.temp <=32:
        #     feels = 'hot'
        # else:
        #     feels = 'baking'
        # output a nicely formatted weather report       format to specific decimal places
        report  = f'The weather in {self.city} is {self.desc} at {self.temp:0.2f}C feels {feels}'
        return report
    def persistToFile(self, filename):
        '''write a weather instance to a text file'''
        fout = open(filename, 'at')
        with fout:
            fout.write( f'{self.__str__()}\n' )


if __name__ == '__main__':
    # exercise this module
    w_gen = Weather('Genoa', 'rainy', 9.04564)
    w_gal = Weather('Galway', 'windy', 6.7045765)
    w_kt  = Weather('Kingston', 'sunny', 27.983083)
   
    print(w_gen)
    print(w_gal)
    print(w_kt)

    w_default = Weather(False, [], ()) # wrong data types so should fall back to the defaults
    print(w_default)

    w_gal.persistToFile('galway_weather.txt')

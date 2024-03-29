"""Classes for working with Temperatures."""

class TemperatureError(Exception):
    """Error raised for invalid temperatures."""

    pass


class Temperature:
    """Represents a temperature.

    Temperatures are expressable in degrees Fahrenheit, degrees celsius,
    or Kelvins.
    """

    def __init__(self, degrees: int = 0):
        """Initialize temperature with specified degrees.

        Args:
            degrees, which can be one of the following:
                (1) a number, or a string containing a number
                    in which case it is interpreted as degrees celsius
                (2) a string containing a number followed by one of the
                    following symbols:
                       C, in which case it is interpreted as degrees celsius
                       F, in which case it is interpreted as degrees Fahrenheit
                       K, in which case it is interpreted as Kelvins

        Raises:
            TemperatureError: if degrees is not one of the specified
                                     forms

        """
        if type(degrees) in (int, float):  # 45.7
            self.celsius = degrees
            return
        if type(degrees) == str and len(degrees)>0 and degrees[-1].lower() == 'c':  # "34C"
            self.celsius = degrees
            return
        if type(degrees) == str and len(degrees)>0:  # "-14.75"
            self.celsius = degrees
            return
        raise TemperatureError(f'Was not able to initialize {degrees}')




    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, new_temp):
        """  Need to support new_temp being: int, float, str or Temperature  
        a.celsius = 32.0
        a.celsius = "32"
        a.celsius = other_temp # Temperature object
        """        
        if type(new_temp) in (int, float):
            self._celsius = float(new_temp)
        if type(new_temp) == str:
            try:
                self._celsius = float(new_temp)
            except ValueError:
                try:
                    if new_temp[-1].lower() == 'c':
                        self._celsius = float(new_temp[:-1])
                    else:
                        raise ValueError('String in wrong format')
                except IndexError:
                    raise ValueError('String is empty')

        if type(new_temp) == Temperature:
            self._celsius = new_temp.celsius
        
        if type(new_temp) not in (int, float, str, Temperature):
            raise TemperatureError("The new temperature wasn't a int, float, str")
    def get_celsius(self):
        """Get the Celsius Temperature"""
        return self.celsius
    @property
    def kelvin(self):
        """Value of Temperature in Kelvin

        When setting kelvin, value must be int, float or string in
        format '345K' or '45'
        """
        return self._celsius + 273.15

    @kelvin.setter
    def kelvin(self, new_temp):
        pass  # Duplicate logic from celsius setter with modifications




    @classmethod
    def average(cls, temperatures):
        """Compute the average of a list of temperatures.

        Args:
            temperatures: a list of Temperature objects
        Returns:
            a Temperature object with average (mean) of the given temperatures

        """
        pass

    def __repr__(self):
        return f'Temperature({self._celsius})'

temp = Temperature(30)
print(temp.get_celsius())
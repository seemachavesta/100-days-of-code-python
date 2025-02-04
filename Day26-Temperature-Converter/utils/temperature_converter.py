class TemperatureConverter:
    """
    A utility class for converting temperatures between Celsius, Fahrenheit, and Kelvin.
    
    """
    @classmethod  
    def celsius_to_fahrenheit(cls, temp: float):
        return round((temp * 9/5) + 32)
         
    @classmethod  
    def fahrenheit_to_celsius(cls, temp: float):
        return round((temp - 32) * 5/9)
        
    @classmethod  
    def celsius_to_kelvin(cls, temp: float):
        return round(temp + 273.15, 2)
        
    @classmethod   
    def kelvin_to_celsius(cls, temp: float):
        return round(temp - 273.15, 2)
        
    @classmethod
    def fahrenheit_to_kelvin(cls, temp: float):
        return round((temp - 32) * 5/9 + 273.15, 2)
        
    @classmethod 
    def kelvin_to_fahrenheit(cls, temp: float):
        return round((temp - 273.15) * 9/5 + 32, 2)
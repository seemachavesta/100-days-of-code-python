import unittest
from temperature_converter import TemperatureConverter

class TestMain(unittest.TestCase):
    
    """ Unit tests for the TemperatureConverter class."""

    def test_celsius_to_fahrenheit(self):
        temp1 = TemperatureConverter.celsius_to_fahrenheit(0)
        temp2 = TemperatureConverter.celsius_to_fahrenheit(100)
        temp3 = TemperatureConverter.celsius_to_fahrenheit(37.78)
        self.assertEqual(temp1, 32.0)
        self.assertEqual(temp2, 212.0)
        self.assertEqual(temp3, 100.0)

    def test_celsius_to_fahrenheit_not_equal(self):
        temp2 = TemperatureConverter.celsius_to_fahrenheit(25)
        self.assertNotEqual(temp2, 32.0)

    def test_fahrenheit_to_celsius(self):
        temp1 = TemperatureConverter.fahrenheit_to_celsius(32)
        temp2 = TemperatureConverter.fahrenheit_to_celsius(98.6)
        self.assertEqual(temp1, 0.0)
        self.assertEqual(temp2, 37.0)

    def test_fahrenheit_to_celsius_not_equal(self):
        temp1 = TemperatureConverter.fahrenheit_to_celsius(32)
        temp2 = TemperatureConverter.fahrenheit_to_celsius(98.6)
        self.assertNotEqual(temp1, 0.5)
        self.assertNotEqual(temp2, 98)

    def test_celsius_to_kelvin(self):
        temp1 = TemperatureConverter.celsius_to_kelvin(0)
        self.assertEqual(temp1, 273.15)

    def test_celsius_to_kelvin_not_equal(self):
        temp1 = TemperatureConverter.celsius_to_kelvin(0)
        self.assertNotEqual(temp1, 273)

    def test_kelvin_to_celsius(self):
        temp1 = TemperatureConverter.kelvin_to_celsius(300)
        temp2 = TemperatureConverter.kelvin_to_celsius(0)
        self.assertEqual(temp1, 26.85)
        self.assertEqual(temp2, -273.15)

    def test_kelvin_to_celsius_not_equal(self):
        temp1 = TemperatureConverter.kelvin_to_celsius(300)
        temp2 = TemperatureConverter.kelvin_to_celsius(0)
        self.assertNotEqual(temp1, 26)
        self.assertNotEqual(temp2, 273.15)
        
    def test_fahrenheit_to_kelvin(self):
        temp1 = TemperatureConverter.fahrenheit_to_kelvin(32)
        self.assertEqual(temp1, 273.15)

    def test_fahrenheit_to_kelvin_not_equal(self):
        temp1 = TemperatureConverter.fahrenheit_to_kelvin(32)
        self.assertNotEqual(temp1, 173)

    def test_kelvin_to_fahrenheit(self):
        temp1 = TemperatureConverter.kelvin_to_fahrenheit(0)
        self.assertEqual(temp1, -459.67)

    def test_kelvin_to_fahrenheit_not_equal(self):
        temp1 = TemperatureConverter.kelvin_to_fahrenheit(0)
        self.assertNotEqual(temp1, 459.67)

    def test_edge_cases(self):
        self.assertEqual(TemperatureConverter.celsius_to_fahrenheit(-40), -40)
        self.assertEqual(TemperatureConverter.fahrenheit_to_celsius(-40), -40)
        self.assertEqual(TemperatureConverter.celsius_to_kelvin(-273.15), 0)





if __name__ == '__main__':
    unittest.main()


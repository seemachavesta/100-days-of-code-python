from utils.temperature_converter import TemperatureConverter


user_menu = """Enter 
 -1 For Celsius To Fahrenheit
 -2 For Fahrenheit to Celsius
 -3 For Kelvin to Celsius
 -4 For Fahrenheit to Kelvin
 -5 For Kelvin to Fahrenheit
 -6 To Quit
Enter your choice: """


def main():
    
    conversion_map = {
        1: ("Celsius To Fahrenheit", TemperatureConverter.celsius_to_fahrenheit),
        2: ("Fahrenheit to Celsius", TemperatureConverter.fahrenheit_to_celsius),
        3: ("Kelvin to Celsius", TemperatureConverter.kelvin_to_celsius),
        4: ("Fahrenheit to Kelvin", TemperatureConverter.fahrenheit_to_kelvin),
        5: ("Kelvin to Fahrenheit", TemperatureConverter.kelvin_to_fahrenheit)
    }

    while True:
        try:
            choice = int(input(user_menu))
            if choice ==  6:
                print('Good bye')
                break
            
            if choice in conversion_map:
                print(f'You choice is {conversion_map[choice][0]}')
                temp = float(input('Enter the temperature: '))
                result = conversion_map[choice][1](temp)
                print(f"The {conversion_map[choice][0]} is: {result:.2f}")
            else:
                print('Invalid Choice, try again.')
                
        except ValueError:
            print('Invalid Input, try again')
        
    
    
if __name__ == "__main__":
    main()
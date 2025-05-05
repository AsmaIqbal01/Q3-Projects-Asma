class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    
if __name__=="__main__":
    celsius_temp =25
    fahrenheit_temp = TemperatureConverter.celsius_to_fahrenheit(celsius_temp)
    print(f"{celsius_temp}°C is equal to {fahrenheit_temp}°F  ")
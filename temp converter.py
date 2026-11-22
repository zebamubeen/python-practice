# celsius_to_fahrenheit
def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

temp = float(input("Enter temperature in Celsius: "))
print(f"{temp}°C is {celsius_to_fahrenheit(temp):.1f}°F") 

# fahrenheit_to_celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

temp_f = float(input("Enter temperature in Fahrenheit: "))
print(f"{temp_f}°F is {fahrenheit_to_celsius(temp_f):.1f}°C")
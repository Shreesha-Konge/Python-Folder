def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5 ) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit -32) * 5/9
temp=int(input('Enter a temparature  : '))
print(f'{temp} Celsius is {celsius_to_fahrenheit(temp)} fahrenheit')
print(f'{temp} Fahrenheit is {fahrenheit_to_celsius(temp)} celsius')
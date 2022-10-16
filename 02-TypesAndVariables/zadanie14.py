temperature = float(input("Enther the temperature in degrees Celcius: "))
temperature1 = temperature + 273 # Kelvin
temperature2 = temperature*9/5 + 32 # Fahrenheit 

print(str(temperature) + "°C = " + str(temperature1) + "K = " + str(temperature2) +"°F")
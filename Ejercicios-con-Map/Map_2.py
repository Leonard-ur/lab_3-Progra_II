celcius = [0 ,10 ,20 , 30]

fahrenheit = list(map(lambda grado: (grado * 9/5) + 32, celcius))

print(fahrenheit)
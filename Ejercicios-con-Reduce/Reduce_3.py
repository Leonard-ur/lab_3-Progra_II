from functools import reduce

numeros = [7, 3, 9, 1, 5]


mayor = reduce(lambda num1, num2: num1 if num1 > num2 else num2, numeros)



print(mayor)
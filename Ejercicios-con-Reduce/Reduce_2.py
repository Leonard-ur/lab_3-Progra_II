from functools import reduce


numeros = [2, 3, 4]

productos = reduce(lambda num1, num2: num1 * num2, numeros)


print(productos)
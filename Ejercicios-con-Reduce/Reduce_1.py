from functools import reduce


numeros = [5, 10 ,15, 20]


sumados = reduce(lambda num1, num2: num1 + num2, numeros)


print(sumados)
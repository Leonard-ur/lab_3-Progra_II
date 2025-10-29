from functools import reduce


cadena = ["Hola", " ","Mundo"]


concatenado = reduce(lambda string1, string2: string1 + string2, cadena)


print(concatenado)
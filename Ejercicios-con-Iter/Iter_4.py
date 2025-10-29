def generador_mayus(cadenas):
    for cadena in cadenas:
        yield cadena.upper()

lista =  ["hola", "python", "es", "genial", "xd"]

iterador = iter(generador_mayus(lista))


for cadena in iterador:
    print(cadena)
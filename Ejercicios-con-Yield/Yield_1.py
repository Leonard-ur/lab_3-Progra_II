#Funcion generadora de numeros pares
def numeros_pares(cantidad=10):
    iteracion = 0
    numero = 0

    while iteracion < cantidad:
        if numero % 2 == 0:
            yield numero
            iteracion += 1
        numero += 1

for par in numeros_pares():
    print(par)
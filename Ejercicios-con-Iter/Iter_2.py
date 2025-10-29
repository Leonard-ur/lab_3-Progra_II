
def generador_impares(inicio=1, fin=20):
    inicio = inicio
    fin = fin
    
    for num in range(inicio, fin):
        if num % 2 != 0:
            yield num
            num +1

for num in generador_impares():
    print(num)
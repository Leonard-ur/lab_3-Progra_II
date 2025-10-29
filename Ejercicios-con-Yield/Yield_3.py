class Cuadrados:
    def __init__(self, inicio = 0, fin=10):
        self.inicio = inicio
        self.fin = fin
    
    def __iter__(self):
        for numero in range(self.inicio, self.fin+1):
            yield numero ** 2


cuadrados_obj = Cuadrados(0, 10)

for cuadrado in cuadrados_obj:
    print(cuadrado)
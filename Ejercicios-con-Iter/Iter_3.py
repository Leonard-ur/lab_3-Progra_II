class generador_cuadrados:
    def __init__(self):
        self.cuadrados = []

    def generador_cuadrados(self, inicio=1, fin=10):
        self.inicio = inicio
        self.fin = fin
        cuadrados = []

        for num in range(self.inicio, self.fin+1):
            cuadrados.append(num * num)
        self.cuadrados = cuadrados
        return cuadrados
    



if __name__ == "__main__":
    generador = generador_cuadrados()

    lista_cuadrados = generador.generador_cuadrados()

    print(lista_cuadrados)

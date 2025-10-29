def fibonacci(limite = 10):
    a = 0
    b = 1
    contador = 0
    limite = limite
    
    while contador < limite:
        yield a
        a, b = b, a + b
        contador += 1



for num in fibonacci():
    print(num)
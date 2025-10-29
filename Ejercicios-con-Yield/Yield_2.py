def numeros_impares(numeros:list):
    for num in numeros:
        if num % 2 != 0:
            yield num



numeros = [1, 22, 69, 60, 133, 67, 911]

for impar in numeros_impares(numeros):
    print(impar)
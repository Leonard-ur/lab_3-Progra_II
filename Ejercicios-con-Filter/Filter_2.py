animales = ["perro", "gato", "pato", "hamster"]

animales_p = list(filter(lambda animal: animal[0].upper()== "P", animales))


print(animales_p)
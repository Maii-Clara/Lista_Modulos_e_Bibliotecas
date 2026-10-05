import random

numero = random.randint(1, 100)
print("Número sorteado:", numero)

filmes = ["Titanic", "Matrix", "Avatar", "Rei Arthur", "Interestelar"]

filme = random.choice(filmes)
print("Filme escolhido:", filme)

random.shuffle(filmes)
print("Lista embaralhada:", filmes)
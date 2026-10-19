from random import randint
import os
from biblioteca import z, somar

x = 5
print(f"o valor de é {x}")

for _ in range(5):
    y = randint(5,12)
    print(y)

x = y + z
print(x)

soma = somar(2,3,5,7)
soma2 = somar(9,11,23,32,45,67,1,2,3,4,5,6)
print(soma,soma2)

texto = "Calor"
print(texto[0]) #C
print(texto[1:4]) #alo
print(texto[:3]) #Cal
print(texto[1:]) #Albr

# Passe por cada letra de uma palavra e indique o n de vogais da mesma
texto = "Rodrigo Silva Arantes"
num_vogais = 0
for letra in texto:
    if letra in "aeiouAEIOU":
        num_vogais = num_vogais +1
print(num_vogais)
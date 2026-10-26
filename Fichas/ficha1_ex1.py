from random import randint

nums = []

for _ in range(30):
    y = randint(1,100)
    nums.append(y)


Npares = 0
Nimpares = 0
Nsuperioramedia = 0
soma = sum(nums)
maior = max(nums)
menor = min(nums)
media = soma / len(nums)
listamedia = []

for num in nums:
    if num % 2 == 0:
        Npares = Npares + 1
    else:
        Nimpares = Nimpares + 1

    if num > media:
        Nsuperioramedia = Nsuperioramedia + 1
        listamedia.append(num)
    else:
        " "

        
print(" A lista completa é ", nums)
print(" Tem ",Npares, " numeros pares") 
print(" Tem ",Nimpares, " numeros impares")
print(" O maior numero é ",maior) 
print(" O menor numero é ",menor) 
print(" A media é ",media) 
print(" A lista tem ", Nsuperioramedia, " numeros maiores que a média") 
print(" A lista superior á média ", listamedia)
 

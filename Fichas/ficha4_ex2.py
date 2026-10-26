resultado ="programação"
Vezes = {}
for caractere in resultado:
    Vezes[caractere] = Vezes.get(caractere, 0) + 1

print(Vezes)
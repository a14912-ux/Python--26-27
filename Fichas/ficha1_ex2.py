from random import randint

notaAlunos = []

for _ in range(15):
    y = randint(0, 20)
    notaAlunos.append(y)

Alunosaprovados = 0
Alunosreprovados = 0
Nsuperioramedia = 0
soma = sum(notaAlunos)
maior = max(notaAlunos)
menor = min(notaAlunos)
media = soma / len(notaAlunos)

for num in notaAlunos:
    if num >= 10:
        Alunosaprovados = Alunosaprovados + 1
    else:
        Alunosreprovados = Alunosreprovados + 1

    if num >= 16:
        Nsuperioramedia = Nsuperioramedia + 1

percentagem = (Alunosaprovados / len(notaAlunos)) * 100

print("Lista de notas:", notaAlunos)
print("Alunos aprovados:", Alunosaprovados)
print("Alunos reprovados:", Alunosreprovados)
print("Alunos com nota igual ou superior a 16:", Nsuperioramedia)
print("A maior nota é:", maior)
print("A menor nota é:", menor)
print("A média da turma é:", media)
print("Percentagem de aprovação:", percentagem, "%")


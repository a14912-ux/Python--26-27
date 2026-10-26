aluno = {
    "Nome": "Ana Silva",
    "Idade": 17,
    "Disciplinas": ["Matemática", "Física", "Informática"],
    "Notas": {"Matemática": 18, "Física": 17, "Informática": 19}
}

aluno["Disciplinas"].append("Português")
aluno["Notas"]["Português"] = 16
aluno["Idade"] = 18

print(aluno["Notas"])

notas_aluno = []
nome_aluno = []

media_notas_aluno = 0.0
soma_notas = 0

for nota in aluno["Notas"].values():
    soma_notas += nota
media_notas_aluno = round(soma_notas / len(aluno["Notas"]),2)
print (f"A média das notas do aluno é: {media_notas_aluno}")
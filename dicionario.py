aluno = { "Nome": "Carlos", "Idade": "17", "Cidade": "Famalicão", "Disciplinas": ["Matemática, Programação, Inglês"],"Notas":{"matematica: [17,5,12]","programação: 18.25"}}
print(aluno["Nome"])

# Alterar valor de uma chave
aluno["Idade"] = 18

# Inserir uma nova chave
aluno["Estado_civil"] = "Solteiro"
print(aluno)

# Imprimir as caracteristicas do aluno
for chave in aluno.keys():
    print()

# Imprimir somente os valores
for valor in aluno.values():
    print(f"{valor}", end = " ")

#Imprimir a chave e o valor
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")

aluno["Disciplinas"].append("Português")
for disciplina in aluno["Disciplinas"]:
    print(disciplina)

#Media de todas as notas
soma = 0
no_notas = 0
for notas_disciplina in aluno ["notas"].values():
    soma += sum(notas_disciplina)
    no_notas += len(notas_disciplina)




import random

jogador = { 
    "Pontos de Vida": 300,
    "Pontos de Ataque  Base": 20, 
    "Poçoes": 2, 
    "Pontos": 0
    }

inimigos = [
    {"Nome": "Goblin", "Pontos de Vida": 40, "Pontos de Ataque": 8, "Pontos": 100},
    {"Nome": "Orc", "Pontos de Vida": 55, "Pontos de Ataque": 11, "Pontos": 200},
    {"Nome": "Troll", "Pontos de Vida": 70, "Pontos de Ataque": 14, "Pontos": 300},
    {"Nome": "Beast", "Pontos de Vida": 85, "Pontos de Ataque": 17, "Pontos": 400},
    {"Nome": "Dragão", "Pontos de Vida": 100, "Pontos de Ataque": 20, "Pontos": 500}
]

for i in range(3):
    numero = random.randint(3, 5)
    inimigo = inimigos
    inimigos.append(inimigo)

def criar_menu():

    print("\n========== BATALHA ==========")
    print("1 - Atacar inimigo")
    print("2 - Estado do jogador")
    print("3 - Listar inimigos vivos")
    print("4 - Usar poção")
    print("5 - Fugir")

    opcao = int(input("Escolhe uma opção: "))
 
  
    if opcao == "1":
        vivos = []

        for inimigo in inimigos:
            if inimigo["Pontos de Vida"] > 0:
                print(inimigo["Pontos de Vida"])

        else:
            print("\nInimigos vivos:")

            for i in range(len(vivos)):
                print(i + 1, "-", vivos[i]["nome"],
                      "Vida:", vivos[i]["vida"])  

            escolha = input("Escolha um inimigo: ")   

    elif opcao == "2":

        print("\n===== Dados Do JOGADOR =====")
        print("Vida:", jogador["Pontos de Vida"])
        print("Pontos:", jogador["pontos"])
        print("Inimigos derrotados:", jogador["derrotados"])
        print("Poções:", jogador["pocoes"])

    elif opcao == "3":

        print("\n===== Dados Do Ininigo =====")
        print("Nome:", inimigo["Nome"])
        print("Vida:", inimigo["Pontos de Vida"])
        print("Pontos:", inimigo["Pontos de Ataque"])

        if len(vivos) == 0:
            print("Não existe inimigos vivos")

    elif opcao == "4":

        if jogador["pocoes"] > 0:

            if jogador["vida"] < 300:

                jogador["vida"] + 25 < 300
                jogador["pocoes"] - 1

                print()

    elif opcao == "5":

        print("Fugiste! O jogo terminou")   


    if jogador["vida"] == 0:

        print("\nFoste derrotado!")

    elif jogador["derrotados"] == len(inimigos):

        print("\nVITÓRIA! Derrotaste todos os inimigos!")

                
            


        
     


    




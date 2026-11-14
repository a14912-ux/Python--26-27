import random

print("========== JOGO DE BATALHA ==========")

jogador = {
    "Pontos de Vida": 300,
    "Pontos de Ataque Base": 20,
    "Pocoes": 2,
    "Pontos": 0,
    "Derrotados": 0
}

inimigos = [
    {"Nome": "Goblin", "Pontos de Vida": 40, "Pontos de Ataque": 8, "Pontos": 100},
    {"Nome": "Orc", "Pontos de Vida": 55, "Pontos de Ataque": 11, "Pontos": 200},
    {"Nome": "Troll", "Pontos de Vida": 70, "Pontos de Ataque": 14, "Pontos": 300},
    {"Nome": "Beast", "Pontos de Vida": 85, "Pontos de Ataque": 17, "Pontos": 400},
    {"Nome": "Dragão", "Pontos de Vida": 100, "Pontos de Ataque": 20, "Pontos": 500}
]

# Escolher aleatoriamente entre 3 e 5 inimigos
quantidade = random.randint(3, 5)
inimigos_escolhidos = random.sample(inimigos, quantidade)


def criar_menu():

    while True:

        print("\n========== BATALHA ==========")
        print("1 - Atacar inimigo")
        print("2 - Consultar estado do jogador")
        print("3 - Listar inimigos vivos")
        print("4 - Usar poção de cura")
        print("5 - Fugir / terminar jogo")

        opcao = input("Escolhe uma opção: ")

        
        if opcao == "1":

            vivos = []

            for inimigo in inimigos_escolhidos:
                if inimigo["Pontos de Vida"] > 0:
                    vivos.append(inimigo)

            if len(vivos) == 0:
                print("Não existem inimigos vivos!")
                

            print("\nInimigos vivos:")

            for i in range(len(vivos)):
                print(i + 1, "-", vivos[i]["Nome"],
                      "Vida:", vivos[i]["Pontos de Vida"])

            escolha = int(input("Escolhe um inimigo: "))


        elif opcao == "2":

            vivos = 0

            for inimigo in inimigos_escolhidos:
                if inimigo["Pontos de Vida"] > 0:
                    vivos += 1

            print("\n===== DADOS DO JOGADOR =====")
            print("Vida:", jogador["Pontos de Vida"])
            print("Pontos:", jogador["Pontos"])
            print("Inimigos derrotados:", jogador["Derrotados"])
            print("Inimigos vivos:", vivos)
            print("Poções:", jogador["Pocoes"])

        elif opcao == "3":

            print("\n===== INIMIGOS VIVOS =====")

            encontrou = False

            for inimigo in inimigos_escolhidos:
                if inimigo["Pontos de Vida"] > 0:
                    print("Nome:", inimigo["Nome"])
                    print("Vida:", inimigo["Pontos de Vida"])
                    print("Ataque:", inimigo["Pontos de Ataque"])
                    print("--------------------")
                    encontrou = True

            if encontrou == False:
                print("Não existem inimigos vivos!")

        elif opcao == "4":

            if jogador["Pocoes"] > 0:

                if jogador["Pontos de Vida"] < 100:

                    jogador["Pontos de Vida"] += 25

                    if jogador["Pontos de Vida"] > 100:
                        jogador["Pontos de Vida"] = 100

                    jogador["Pocoes"] -= 1

                    print("Usaste uma poção!")
                    print("Vida atual:", jogador["Pontos de Vida"])

                else:
                    print("Já tens a vida cheia!")

            else:
                print("Não tens poções disponíveis!")

        elif opcao == "5":

            print("Fugiste! A partida terminou por fuga.")
            break

        else:
            print("Opção inválida!")

        if jogador["Pontos de Vida"] == 0:
            print("\nFoste derrotado!")
            break

        if jogador["Derrotados"] == len(inimigos_escolhidos):
            print("\nVITÓRIA! Derrotaste todos os inimigos!")
            break



criar_menu()

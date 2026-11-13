
import random

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

# Escolher 3 inimigos aleatórios
inimigos_escolhidos = random.sample(inimigos, 3)


def criar_menu():

    while True:

        print("\n========== BATALHA ==========")
        print("1 - Atacar inimigo")
        print("2 - Estado do jogador")
        print("3 - Listar inimigos vivos")
        print("4 - Usar poção")
        print("5 - Fugir")

        opcao = input("Escolhe uma opção: ")

        if opcao == "1":

            vivos = []

            for inimigo in inimigos_escolhidos:
                if inimigo["Pontos de Vida"] > 0:
                    vivos.append(inimigo)

            if len(vivos) == 0:
                print("Não existem inimigos vivos!")
                continue

            print("\nInimigos vivos:")

            for i in range(len(vivos)):
                print(i + 1, "-", vivos[i]["Nome"],
                      "Vida:", vivos[i]["Pontos de Vida"])

            try:
                escolha = int(input("Escolhe um inimigo: "))
            except ValueError:
                print("Escolha inválida!")
                continue

            if escolha < 1 or escolha > len(vivos):
                print("Inimigo inválido!")
                continue

            inimigo = vivos[escolha - 1]

            dano = jogador["Pontos de Ataque Base"]
            inimigo["Pontos de Vida"] -= dano

            print("\nAtacaste o", inimigo["Nome"], "e causaste", dano, "de dano!")

            if inimigo["Pontos de Vida"] <= 0:
                inimigo["Pontos de Vida"] = 0
                print("Derrotaste o", inimigo["Nome"], "!")
                jogador["Pontos"] += inimigo["Pontos"]
                jogador["Derrotados"] += 1

            else:
                print("Vida restante:", inimigo["Pontos de Vida"])

                dano_inimigo = inimigo["Pontos de Ataque"]
                jogador["Pontos de Vida"] -= dano_inimigo

                print("O", inimigo["Nome"], "atacou-te e causou",
                      dano_inimigo, "de dano!")

        elif opcao == "2":

            print("\n===== DADOS DO JOGADOR =====")
            print("Vida:", jogador["Pontos de Vida"])
            print("Pontos:", jogador["Pontos"])
            print("Inimigos derrotados:", jogador["Derrotados"])
            print("Poções:", jogador["Pocoes"])

        elif opcao == "3":

            print("\n===== INIMIGOS VIVOS =====")

            vivos = [i for i in inimigos_escolhidos
                     if i["Pontos de Vida"] > 0]

            if len(vivos) == 0:
                print("Não existem inimigos vivos!")
            else:
                for inimigo in vivos:
                    print("Nome:", inimigo["Nome"])
                    print("Vida:", inimigo["Pontos de Vida"])
                    print("Ataque:", inimigo["Pontos de Ataque"])
                    print("--------------------")

        elif opcao == "4":

            if jogador["Pocoes"] > 0:

                if jogador["Pontos de Vida"] < 300:

                    jogador["Pontos de Vida"] = min(
                        300, jogador["Pontos de Vida"] + 25
                    )

                    jogador["Pocoes"] -= 1

                    print("Usaste uma poção!")
                    print("Vida atual:", jogador["Pontos de Vida"])

                else:
                    print("Já tens a vida cheia!")

            else:
                print("Não tens poções disponíveis!")

        elif opcao == "5":

            print("Fugiste! O jogo terminou.")
            break

        else:
            print("Opção inválida!")

        if jogador["Pontos de Vida"] <= 0:
            print("\nFoste derrotado!")
            break

        elif jogador["Derrotados"] == len(inimigos_escolhidos):
            print("\nVITÓRIA! Derrotaste todos os inimigos!")
            break


criar_menu()

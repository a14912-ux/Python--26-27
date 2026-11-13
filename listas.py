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
    numero = random.randint(0, 4)
    inimigo = inimigos[numero]
    inimigos.append(inimigo)

def criar_menu():
    print("\n========== BATALHA ==========")
    print("1 - Atacar Inimigo")
    print("2 - Consultar Estado do jogador")
    print("3 - Listar Inimigos Vivos")
    print("4 - Usar Poção de Cura")
    print("5 - Fugir / Terminar Jogo")

def atacar_inimigos():
    vivos = []

    for inimigo in inimigos:
        if inimigo ["Pontos de Vida"] > 0:
            vivos.append(inimigo)

    if vivos == 0:
        print("Não existe inimigos vivos")
        return

    for i in range(len(vivos)):
        print(i + 1, "-", vivos[i]["Nome"])

    escolha = int(input("Escolhe um inimigo: "))

    
    inimigo = vivos[escolha - 1]

    dano = random.randint(10, 20)

    inimigo["Pontos de Vida"] = max(0, inimigo["Pontos de Vida"] - dano)


    



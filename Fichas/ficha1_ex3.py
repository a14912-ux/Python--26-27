from random import randint
import os

jogar = "S"

pontosJogador = 0

while jogar == "S":
    numero_secreto = randint(1, 100)
    print(numero_secreto)
    tentativas = 0
    acertou = False
    pontos = 0
    meuNumero = 0
    jogarNovamente = 0

    print("\n ***Adivinha o numero*** \n")
    print("Tente adivinhar o número entre 1 e 100.")

    while tentativas < 7:
        meuNumero = int(input("Tente o valor gerado: "))

        while meuNumero < 1 or meuNumero > 100:
            print("Valor inválido! Tem de ser entre 1 e 100")
            meuNumero = int(input("Tente novamente: "))
            print("")

        tentativas = tentativas + 1

        if meuNumero == numero_secreto:
            print(f"Parabéns, acertaste em {tentativas} tentativas")
            acertou = True
            break

        if numero_secreto > meuNumero:
            print("O numero gerado é maior")
        else:
            print("O numero gerado é menor")

    if acertou == False:
        print(f"Que triste! O numero gerado era {numero_secreto}")

    if acertou == True:
        if tentativas == 1:
            pontosJogador = pontosJogador + 100
        elif tentativas == 2:
            pontosJogador = pontosJogador + 80
        elif tentativas == 3:
            pontosJogador = pontosJogador + 60
        elif tentativas == 4:
            pontosJogador = pontosJogador + 40
        elif tentativas == 5:
            pontosJogador = pontosJogador + 30
        elif tentativas == 6:
            pontosJogador = pontosJogador + 20
        elif tentativas == 7:
            pontosJogador = pontosJogador + 10

        print(f"Conseguiste {pontosJogador} pontos")
        print("")

    jogar = input("Deseja jogar novamente? (S/N) ").upper()

print(f"Pontuação final: {pontosJogador} pontos")
print("")

        





    



    




    
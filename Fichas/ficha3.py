nums = [i for i in range(1, 11)]
nums2 = [i for i in range(5, 21)]
numeros = [1,2,3,4,5,6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
nome = 'MarcelO ViEiRa amorIM'
nomes = ["Antonio", "Ana","Joao","Amelia"]
frutas = ["Amora","Maça","Pessego","Pera"]
divisor = 3
quadrados = []
tamanho = []

numeros_pares = [num for num in nums if num % 2 == 0]
quadrados = [num*num for num in nums]
print("Numeros pares:" ,numeros_pares, "Respetivo numero ao quadrado:", quadrados)

carros =["BMW","Porshe","Opel Astra","Ferrari"]
letras_carros = [len(carro) for carro in carros]
print("Numero de letras de cada carro:" ,letras_carros)

numeros2 = [numeros for numeros in range(1,21) if numeros > 5]
print(numeros2)

letras_maiusculas = [ letra for letra in nome if letra.isupper()]
print(letras_maiusculas)

resultado = [x * 2 if x % divisor == 0 else x for x in numeros]
print(resultado)

comeca_com_A = [nome for nome in nomes if nome.startswith("A")]
print(comeca_com_A)

menos_5_letras = [len(fruta) for fruta in frutas if len(fruta) > 5 ]
print(menos_5_letras)









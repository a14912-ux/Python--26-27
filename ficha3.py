nums = [i for i in range(1, 11)]
nums2 = [i for i in range(5, 21)]
quadrados = []
tamanho = []

numeros_pares = [num for num in nums if num % 2 == 0]
quadrados = [num*num for num in nums]
print("Numeros pares:" ,numeros_pares, "Respetivo numero ao quadrado:", quadrados)

carros =["BMW","Porshe","Opel Astra","Ferrari"]
letras_carros = [len(carro) for carro in carros]
print("Numero de letras de cada carro:" ,letras_carros)





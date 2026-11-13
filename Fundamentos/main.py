from fuctions import add, update_final_price, print_product, menu
import os

products = []

escolha = menu()

while( escolha != 5):
    match (escolha):
        case 1:

            produto = input("Indique o nome do produto: ")
            preco = float(input("Indique o preco do produto:  "))
            iva = float(input("Indique o iva: "))
            products.append(add(produto,preco,iva))

        case 2:

          for product in products:
             print(print_product(product))
          x = input("Prime uma tecla para continuar ...")

        case 3:
        
         for product in products:
            update_final_price(product)
        
        case 4:

            encontrei = False
            pesquisa = input("Produto a listar: ")
            for p in products:
               if p["products"] == pesquisa:
                  print(print_product(p))
                  encontrei = True
            if not encontrei:
               print("este produto nao faz parte da lista")

            x = input("Prima uma tecla para continuar ...")

        case 5:
       
             break
    os.system("cls") 
    escolha = menu()


            






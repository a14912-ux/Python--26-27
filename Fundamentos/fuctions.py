def add(produto,preco,iva=0.23):
    return {
        "product": produto,
          "price": preco, 
          "tax": iva
          
        }   

def update_final_price(d):
    d["final_price"] = round(d["price"] * (1 + d["tax"]), 2)

def print_product(d):
    print(f"O Produto {d['product']} com o preco {d['price']} e iva de {d['tax']}:")

def menu():
    print("-----Menu de opções-----")
    print("1 - Adicionar produto")
    print("2 - Listar produtos")
    print("3 - Atualizar preços")
    print("4 - Imprimir produto")
    print("5 - Sair")
    op = int(input("Escolha uma opção: "))
    return op


    

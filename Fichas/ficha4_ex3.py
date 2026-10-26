biblioteca = {
    "livro1": {
        "titulo": "Python Fluente",
        "autor": "Luciano Ramalho",
        "ano": 2015,
        "disponivel": True
    },
    "livro2": {
        "titulo": "Pense em Python",
        "autor": "Allen B. Downey",
        "ano": 2015,
        "disponivel": True
    },
    "livro3": {
        "titulo": "Introducão à Programação com Python",
        "autor": "Nilo Ney Coutinho Menezes",
        "ano": 2019,
        "disponivel": False
    }
}

#print(biblioteca["livro1"]["titulo"])
#print(biblioteca["livro2"]["titulo"])
#print(biblioteca["livro3"]["titulo"])

#biblioteca["livro4"] = {
    #"titulo": "Python para Todos",
    #"autor": "Charles Severance",
    #"ano": 2016,
    #"disponivel": True
#}
#print(biblioteca)

biblioteca["livro1"]["disponivel"] = False

for chave, valor in biblioteca.items():
    print(f"{valor['titulo']}: {valor['autor']}")

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


print(" 1. Livros Disponíveis ")
for livro, dados in biblioteca.items():
    if dados["disponivel"]:
        print(dados["titulo"])


biblioteca["livro4"] = {
    "titulo": "Python para Todos",
    "autor": "Charles Severance",
    "ano": 2016,
    "disponivel": True
}

biblioteca["livro1"]["disponivel"] = False

livros_luciano = []
for livro, dados in biblioteca.items():
    if dados["autor"] == "Luciano Ramalho":
        livros_luciano.append(dados["titulo"])

print(" 4. Livros do Luciano Ramalho ")
print(livros_luciano)


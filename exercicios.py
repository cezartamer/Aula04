##lista de números ao quadrado

# lista: list = [1,2,3,4,5,6,7,8,9,10]

# for i in lista:
#     print(i **2)

## outra maneira de fazer o o exec.:
# lista = [item**2 for item in range(10)]
# print(lista)


##mudificar lista de liguagens

# lista: list = ['Java', 'C#', 'Python', 'C++']

# lista.remove("C#")
# lista.append("Ruby")

# print(lista)

##Contar a ocorrencia de caracteres

# def contar_occorencia_de_caracteres(caractere):
#     contagem = dict()
#     for cont in caractere:
#         print(f"{cont} = {contagem.get(cont,0)+1}")
#         contagem[cont] = contagem.get(cont,0)+1
#     return contagem

# print(contar_occorencia_de_caracteres("Engenheiro de dados"))

# dic = dict()
# lista = ['A', 'B']
# valor = lista[1]
# dic[valor] =  dic.get(valor,0)+1
# dic[valor] =  dic.get(valor,0)+1
# dic[valor] =  dic.get(valor,0)
# print(dic)

## teste
# lista = ['cezar','tamer',1]

# lista = [str(palavra).upper() for palavra in lista]

# print(lista)

# lista = ['Ferrari', 'Lamborghini', 'Porsche']
# dicionario = {
#   elemento.lower(): f'Montadora: {elemento.upper()}' for elemento in lista
# }
# print(dicionario)


##Lista de comprars

# lista_compras = ["maçã", "banana", "cereja"]
# precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
# total = sum(precos[item] for item in lista_compras)
# print(f"Preço total: {total}")


# cars = ['Ford', 'BMW', 'Volvo', 'Tesla']

# cars.sort(reverse=True)

# print(cars)

##Ordenar por nome

# pessoas = [
#     {"nome": "Carol", "idade": 30},
#     {"nome": "Bob", "idade": 25},
#     {"nome": "Alice", "idade": 20}
# ]
# pessoas.sort(key=lambda pessoa: pessoa["nome"])

# print(pessoas)


dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"c": 3, "d": 4}

dicionario_fundido = {**dicionario1, **dicionario2}

print(dicionario_fundido)
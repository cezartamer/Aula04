import csv

caminho: str = 'exemplo.csv'

arquivo_csv: list = []

with open(file = caminho, mode ="r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        arquivo_csv.append(linha)
    
print(arquivo_csv)




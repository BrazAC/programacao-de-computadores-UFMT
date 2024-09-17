"""
Aluno: Braz Amorim
Professor: Ivairton
Data 04/09

"""
#Importando biblioteca para apagar e renomear arquivos
import os

#Acessando arquivo a ser atualizado
contas = open("./contas.txt", mode="r")
#Criando arquivo temporario (que se tornara o definitivo)
temp_file = open("./temp_file.txt", mode="w")

with contas, temp_file:
    for linha in contas:
        id, nick, data = linha.split()
        if id != "2754": #Se o if da conta nao for o que eu quero atualizar...
            #Apenas copiar a linha do arquivo original para o temp
            temp_file.write(linha)
        else: #Se o id da conta for o que eu quero atualizar...
            #Escrever linha atualizada (atualizar nick) em temp
            temp_file.write(f"{id} oErmoAmante {data}\n")

#Remover antigo arquivo principal
os.remove("./contas.txt")
#Renomear temp para ser o novo contas (arquivo principal)
os.rename("./temp_file.txt", "./contas.txt")
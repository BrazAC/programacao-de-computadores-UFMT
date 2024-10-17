import sys
from Class_produto import Produto
from Class_estoque import Estoque

import os

def cadastraProdutos(all_data, estoque):
    for linha in range(len(all_data)):
        if all_data[linha] == "":
            #Criar novo produto
            novoProduto = Produto()
        else:
            #Cadastrar informações
            if all_data[linha] == "NOME":
                #Cadastrar nome
                novoProduto.nome = all_data[linha + 1]
            elif all_data[linha] == "CODIGO":
                #Cadastrar codigo
                novoProduto.codigo = int(all_data[linha + 1])
            elif all_data[linha] == "PRECO":
                #Cadastrar preco
                novoProduto.preco = float(all_data[linha + 1])
            elif all_data[linha] == "QUANTIDADE":
                #Cadastrar quantidade
                novoProduto.quantidade = int(all_data[linha + 1])
            
                #Cadastrar novoProduto no estoque
                estoque.produtos.append(novoProduto)
    return estoque
    
def mostraRelatorio(estoque):
    subtotalTotal = 0
    print("")
    print("=======RELATORIO=======")
    for i in range(len(estoque.produtos)):
        #Mostrar informações do produto atual
        print("")
        print("Codigo: ", estoque.produtos[i].codigo)
        print("Nome: ", estoque.produtos[i].nome)
        print("Preco unitario: ", estoque.produtos[i].preco)
        print("Quantidade: ", estoque.produtos[i].quantidade)
        print("Subtotal: ", estoque.produtos[i].quantidade * estoque.produtos[i].preco)

        subtotalTotal += estoque.produtos[i].quantidade * estoque.produtos[i].preco
    
    #Mostrar total de subtotais
    print("Subtotal total: ", subtotalTotal)
    print("=======================")

def incrementaQuantidade(produto, quantidade):
    produto.quantidade += quantidade

def decrementaQuantidade(produto, quantidade):
    produto.quantidade -= quantidade

def encontraProduto(codigoProduto, estoque):
    for i in range(len(estoque.produtos)):
        if codigoProduto == estoque.produtos[i].codigo:
            return estoque.produtos[i]

def main():
    clearTerminal = lambda: os.system('clear')
    clearTerminal()

    if (sys.argv.__len__() != 2):
        print("ERROR invalid argument ammount")
        return
    else:
        #Abrir arquivo / Extrair informações linha a linha / Fechar arquivo
        file_name = open(sys.argv[1], 'r') 
        all_data = file_name.readlines() #["Dados linha 1", "Dados linha 1", "..."]
        file_name.close() 

        #Remover os caracteres de quebra de linha 
        all_data = [line.strip() for line in all_data]

        #Cadastrar produtos
        estoque = Estoque()
        estoque = cadastraProdutos(all_data, estoque)  
        
        #Iniciar menu com sentinela
        sentinela = 1
        while sentinela:
            print("----------- CONTROLE DE ESTOQUE MEGA 2000 -----------")
            print("Escolha uma opcao:")
            print("1 - Incrementar quantidade")
            print("2 - Decrementar quantidade")
            print("3 - Gerar relatorio")
            print("0 - Sair")
            opcao = int(input("ESCOLHA: "))
            clearTerminal()

            if opcao == 0:
                sentinela = 0
            elif opcao == 1:
                #Obter o codigo do produto / quantidade a ser incrementada
                codigoProduto = int(input("Insira o codigo do produto: "))
                quantidade = int(input("Insira a quantidade a ser incrementada: "))

                #Encontrar o produto correspondente
                produto = encontraProduto(codigoProduto, estoque)

                #Incrementar quantidade
                incrementaQuantidade(produto, quantidade)
                clearTerminal()

            elif opcao == 2:
                #Obter o codigo do produto / quantidade a ser incrementada
                codigoProduto = int(input("Insira o codigo do produto: "))
                quantidade = int(input("Insira a quantidade a ser decrementada: "))

                #Encontrar o produto correspondente
                produto = encontraProduto(codigoProduto, estoque)

                #Decrementar quantidade
                decrementaQuantidade(produto, quantidade)
                clearTerminal()

            elif opcao == 3:
                mostraRelatorio(estoque)
                _ = input("Pressione qualquer tecla para voltar ao menu")
                clearTerminal()

if __name__ == "__main__":
    main()
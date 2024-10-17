import sys
from Class_acao_carteira import ActionWallet
from Class_acao import Action
from Class_data import Data

#Algoritm
'''
Extrair as informações do arquivo
Cadastrar informações em registros
Obter o nome e valor atualizado das ações, comparar com os antigos
Retornar um relatorio com a % de diferença e se ouve lucro ou perca
'''

def setupInRegisters(all_data):
    for lineNumber in range(len(all_data)):
        if all_data[lineNumber] == "":
            #Criar nova acao
            newAction = Action
            #Cadastrar nome da acao
            newAction.name = all_data[lineNumber + 1]
            #Cadastrar sigla da acao
            newAction.nick = all_data[lineNumber + 2]
            #Cadastrar valor da acao
            newAction.value = 20

            #Criar nova acaoCarteira
            actionWallet = ActionWallet
            #Cadastrar acao operada
            actionWallet.action = newAction
            #Cadastrar data de operacao
            actionWallet.buyDate = all_data[lineNumber + 3]
            #Cadastrar valor da operacao
            actionWallet.buyValue = all_data[lineNumber + 4]

def main():
    if (sys.argv.__len__() != 2):
        print("ERROR invalid argument ammount")
        return # Encerra a execucao do programa
    else:
        #Extrair informações do arquivo
        file_name = open(sys.argv[1], 'r') # abre o arquivo para leitura
        all_data = file_name.readlines() # le todas as linhas do arquivo. Pode-se usar outra estrategia de ler linha a linha
        file_name.close() # apos a leitura dos dados fecha o arquivo
        all_data = [line.strip() for line in all_data] # remove os caracteres de quebra de linha 

        for line in all_data:
            print(line)

        #Cadastrar informações nos registros        
        setupInRegisters(all_data)

        #Obter novos valores da acoes, gerar relatorio
        



if __name__ == "__main__":
    main()
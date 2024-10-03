"""
Aluno: 03/10/24
Professor: Ivairton
Aluno: Braz Amorim

OBS:
Não misturar tipos de dados diferentes na mesma estrutura de dados
Usar uma estrutura de dados para cada tipo de informação 
    ex: 
    um vetor para alunos
    um vetor para notas
    uma variavel para nome da turma


Exemplo de arquivo de entrada:
TURMA:
TURMA DO IVAIRTON
ALUNOS:
JOÃO 7.5 4.8
MARIA 9.5 8.0
JOSÉ 7.9 9.8

TURMA:
TURMA 2023/1 A
ALUNOS:
ANA 10.0 8.0
MARIO 5.9 9.0

TURMA:
TURMA DO IVAIRTON
ALUNOS:
JOÃO 7.5 4.8
MARIA 9.5 8.0
JOSÉ 7.9 9.8

TURMA:
SOU UM NOME QUALQUER
ALUNOS:
ANA 10.0 8.0
MARIO 5.9 9.0
"""

#Algoritmo (meio nas coxa)
'''
Criar logica para entregar como parametro na chamada do programa o nome do arquivo
Guardar arquivo em arqvEntrada
#Obter dados 
Abrir arqvEntrada: 
    #Guardar dados em uma matriz
    Iterar pelas linhas de arqvEntrada:
        Se linha != "TURMA:" e linha != "ALUNOS:":
            splitar linha em nome, v1, v2
                Se nome == "TURMA":
                    #obter informações sobre a turma
                    splitar linha em: _, ano, letraTurma
                    guardar dados splitados em um vetor, guardar vetor em dadosTurma
                senao:
                    #obter informações sobre o aluno
                    splitar linha em: nome, n1, n2
                    guardar dados splitados em um vetor, guardar vetor no final de dadosTurma
                """
                    nome, v1, v2  = linha.split()
                    if nome == "TURMA":
                        #Adicionar identificação da turma em dadosTurma
                        # _, ano, letra
                        dadosTurma.append(linha.split())
                    else:
                        #Adicionar dados do aluno em dadosTurma
                        dadosTurma.append(linha.split())
                """

        Senao se linha == "TURMA:":
            criar (nova) matriz dadosTurma
    #Guardar dados em um arquivo, depois limpar a matriz
    Criar arquivo com nome: "ano/letraTurma.txt"
    Guardar arquivo em arqvSaidaMedias
    Abrir arqvSaidaMedias:
        Adicionar a arqvSaidaMedias os dados que estao em dadosTurma 
'''

#Algoritmo 2.0
"""

"""

#Importando biblioteca para usar funções do SO
import sys

#Declarando funcoes
def criaArqMediasTurma(dadosTurma):
    arquvMedias = open(f"./medias-{dadosTurma[0][1]}-{dadosTurma[0][2]}.txt", mode="w")
    with arquvMedias:
        for l in range(1, len(dadosTurma)):
            nome, n1, n2 = dadosTurma[l].split()
            media = (n1 + n2)/2
            if media >= 5:
                situacao = "APROVADO"
            else:
                situacao = "REPROVADO"
            arquvMedias.write(f'{nome} {media} {situacao}\n')
    print("Arquivo criado!")

def main():
    #Logica para capturar os argumentos diretamente na chamada do programa
    if (sys.argv.__len__() == 2): #Se a quantidade de argumentos esta correta
        #Guardar arquivo em arqvEntrada
        arqvEntrada = open(f"./{sys.argv[1]}", mode="r")

        #Abrindo arquivo para obter dados
        with arqvEntrada:
            print("Abriu arquivo!")
            #Iterando pelas linhas de arqvEntrada:
            for linha in arqvEntrada:
                print("Iterando pelo arquivo")
                #Obter e guardar dados na mtz alunos
                if linha != "TURMA:" and linha != "ALUNOS:":
                    dadosTurma.append(linha.split())
                elif linha == "TURMA:":
                    #Criar mtz dadosTurma
                    dadosTurma = []
                elif linha == "":
                    #Escrever dados no arquivo de texto da turma
                    criaArqMediasTurma(dadosTurma)

            print("Fechou arquivo!")     
    else:
        print("Error: Invalid args ammount")

if __name__ == "__main__":
    main()

'''
    print("Informe o nome do arquivo:")
    print(f"Ex: python3 {sys.argv[0]} turmas.txt") #O valor do primeiro argumento é sempre o nome do próprio programa

    #Logica para capturar os argumentos diretamente na chamada do programa
    if (sys.argv.__len__() == 2): #Analisando o tamanho da lista dos valores de argumentos
        print("Certa quantidade de argumentos, prosseguir com programa")
        return #Encerra a execução do programa
    else:
        ...
'''
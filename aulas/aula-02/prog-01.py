"""
UFMT - Bacharelado em CIencia da COmputacao
Programacao de computadores
Prof. Ivairton
15/08/2024

Programa:
- Leia do usuário um valor inteiro positivo (verifique) que irá descrever quanto valores
(reais) serão lidos. 
- Etnão, leia todos os valores prevstos e etnão calcule a somatória 
e a média entre os valores informados.
"""

#Meu Algoritmo
'''
1 - Ler dado do usuario, se o dado for inteiro positivo guarda-lo em x
2 - Ler mais dados x vezes
3 - Calcular a somatoria e a media
4 - Mostrar o resultado dos calculos
'''


def main():
    #Criando variaveis do somatorio e a media
    somatorio = 0


    #Obtendo quantidade de leituras obrigatoriamente >= 0
    condicao = True
    while condicao:
        condicao = False
        quantLeituras = int(input("Insira a quantidade de leituras (inteiro>0): "))
        if quantLeituras >= 0:
            condicao = False
            #Entrada maior que zero, sair do looping
        else:
            print("Insira um número inteiro positivo!")
            condicao = True
            #Re-executar pedido da quantidade
    
    #Lendo mais x's entradas (apenas quando x>=0)
    for contador in range(0, quantLeituras):
        valor = float(input(f'Insira o valor {contador}: '))
        somatorio += valor

    #Mostrar Media e somatorio
    print(f'Media: {somatorio/quantLeituras}')
    print(f'Somatorio: {somatorio}')
    

if __name__ == "__main__":
    main()

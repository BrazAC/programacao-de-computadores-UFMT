"""
UFMT - Bacharelado em Ciencia da Computacao
Programacao de computadores
Prof. Ivairton
21/08/2024

Programa:
Escreva um programa que defina um loop no qual são iseridos 4 inteiros. 
O programa deve exibir a soma, a média, o produto, o menor e o maior desses valores fornecidos.
"""
#Algoritmo
"""
Repetir 4 vezes:
    1 - Receber valor inteiro
    2 - Guardar valor recebido no final de listaVal
    3 - Somar o valor inteiro em somaVal
    4 - Multiplicar o valor inteiro em prodVal
1 - Exibir a soma obtida no loop
2 - Exibir a média dos valores obtidos no loop
3 - Exibir o produto dos valores obtido no loop
4 - Descobrir e mostrar o menor valor de listaVal
5 - Descobrir e mostrar o maior valor de listaVal
"""

def main():
    cont = 0
    somaVal = 0
    prodVal = 1
    listaVal = []

    #Obtendo valores
    while cont <= 3:
        cont += 1
        val = int(input(f"Insira o valor inteiro {cont}: "))
        listaVal.append(val)
        somaVal += val          
        prodVal *= val
    
    #Verificando qual o menor e maior numero
    menorVal = listaVal[0]
    maiorVal = listaVal[0]
    
    for valor in listaVal:
        if valor <= menorVal:
            menorVal = valor
        if valor >= maiorVal:
            maiorVal = valor
                
    #Mostrando valores
    print(f"Seu somatorio foi: {somaVal}")
    print(f"Seu produtorio foi: {prodVal}")
    print(f"Sua media foi: {somaVal/4}")
    print(f"O maior valor: {maiorVal}")
    print(f"O menor valor: {menorVal}")

if __name__ == "__main__":
    main()
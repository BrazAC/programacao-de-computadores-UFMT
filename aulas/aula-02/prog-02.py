"""
UFMT - Bacharelado em CIencia da COmputacao
Programacao de computadores
Prof. Ivairton
15/08/2024

Programa:
Leia do usuário dois valores inteiros positivos (verifique) e então imprima a tabuada entre os dois valores.
"""

#Meu algoritmo
'''
1 - Obter primeiro valor, verificar se e >= 0
2 - Obter segundo valor, verificar se e >= 0
3 - Se ambos valores forem >= 0
    3.1 - Mostrar os produtos do valor primeiro por 0 até 10
    3.1 - Mostrar os produtos do segundo por 0 até 10
'''

def main():
   
    #Obter primeiro , verificar se e >= 0
    print("---SUPER GERADOR DE TABUADA---")
    val1 = int(input("Insira o primeiro valor: "))
    val2 = int(input("Insira o segundo valor: "))
    print("------------------------------")
    if val1 >= 0 and val2 >= 0:
        #ambos valores >= 0, mostrar tabuadas
        for cont in range(11):
            print(f'{val1} * {cont}: {cont*val1}')
        print("------------------------------")
        for cont in range(11):
            print(f'{val2} * {cont}: {cont*val2}')
    else:
        print("Insira um inteiro positivo!")

        
        



if __name__ ==  "__main__":
    main()
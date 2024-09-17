"""
UFMT - Campus Araguaia
Aluno: Braz Amorim Campos
Data: 05/09/2024
Professor: Ivairton


Exercicio:
Escreva uma funcao recursiva que calcule a multiplicacao entre dois valores
por meio de sucessivas somas:
3 * 4 = 3 + 3 + 3 + 3
"""
#Algoritmo
"""
1 - Receber ambos os valores do produto
2 - Verificar qual o menor deles, somar ele com ele mesmo a quantidade do outro
"""

def main():
    #Receber valores inteiros
    v1 = int(input())
    v2 = int(input())

    #Chamando funcao
    #print(produto(v1, v2))


    #Encontrar o menor valor entre eles?
    #Se a funcao ja receber o menor e o maior valor, ela ira executar a menor quantidade de somas possiveis
    if v1 <= v2:
        print(produto(v1, v2))
    elif v1 >= v2:
        print(produto(v2, v1))
    

def produto(menorVal, maiorVal):
    if menorVal ==  0 or maiorVal == 0:
        return 0
    elif menorVal == 1:
        return maiorVal
    else: #Numeros menores que 0 e maiores que 1
        print()
        #Se um deles for negativo
            #Identificar qual e negativo
                #Tornar o negativo positivo, obter a soma e retornar
        #Se nenhum deles for negativo
            #Obter a soma e retornar

if __name__ == "__main__":
    main()

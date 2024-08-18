"""
UFMT - Bacharelado em Ciencia da Computacao
Programacao de computadores
Prof. Ivairton
18/08/2024

Programa:
Escreva um script que solicite três números de ponto flutuante diferentes para o usuário. 
Em seguida, exiba os números em ordem crescente. 
Lembre-se de que um conjunto de instruções if pode conter mais de uma instrução. 
Prove que seu script funciona executando-o em todas as seis ordenações possíveis dos números. 
Desafio extra: Seu script funciona com números duplicados?
"""

#Algoritmo
'''
1 - Receber numeros float x, y, z
2 - Verificar se x == y ou x == z ou y == z (se algum numero e igual ao outro)
    Se x == y
        Se x ou y < z
            Saida: x, y, z
        Contrario
            Saida: z, x, y
    Se x == z
        Se x ou z < y
            Saida: x, z, y
        Contrario
            Saida: y, x, z
    Contrario (z == y)
        Se z ou y < x
            Saida: z, y, x
        Contrario
            Saida: x, z, y
3 - Se todos forem diferentes
    Se x < y e x < z
        Se y < z
            Saida x, y, z
        Contrario
            Saida x, z, y
    Se y < x e y < z
        Se x < z
            Saida: y, x, z
        Contrario
            Saida: y, z, x
    Contrario (z < x e z < y)
        Se x < y
            Saida: z, x, y
        Contrario
            Saida: z, y, x

'''
def main():
    x = float(input("Insira um numero real: "))
    y = float(input("Insira um numero real: "))
    z = float(input("Insira um numero real: "))

    if x == y or x == z or y == z: #Alguem e igual a alguem
        if x == y:
            if x < z:
                print(x, y, z)
            else:
                print(z, x, y)
        elif x == z:
            if x < y:
                print(x, z, y)
            else:
                print(y, z, x)
        else: #y == z
            if y < x:
                print(y, z, x)
            else:
                print(x, y, z)
    else: #Todos diferentes entre si
        if x < y and x < z:
            if y < z:
                print(x, y, z)
            else:
                print(x, z, y)
        elif y < x and y < z:
            if x < z:
                print(y, x, z)
            else:
                print(y, z, x)
        else: #z < x and z < y
            if x < y:
                print(z, x, y)
            else:
                print(z, y, x)


if __name__ == "__main__":
    main()
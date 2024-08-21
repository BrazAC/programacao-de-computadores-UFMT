"""
UFMT - Bacharelado em Ciencia da Computacao
Programacao de computadores
Prof. Ivairton
17/08/2024

Programa:
Escreva um script que solicite ao usuário um número inteiro de cinco dígitos. 
Em seguida, separe o número em seus dígitos individuais e os imprima, separados entre si por três espaços. 
Por exemplo, se o usuário digitar o número 42339, o script deverá imprimir 4 2 3 3 9. 
Suponha que o usuário entre com o número correto de dígitos. 
Dica: Use as operações de divisão inteira e módulo para separar os dígitos.
"""

#Algoritmo semi-inutil (faz a mesma coisa que o final, só que da direita pra esquerda do número)
'''
1 - Obter o numero de cinco digitos, guardar em val  

Repetir de 2 -> 7
2 - Obter o ultimo algarismo (val % 10) e guardar em ultAlg 
3 - Subtrair de val o ultAlg
4 - dividir val por 10
5 - Somo ultAlg com valFinal (valFinal inicia como 0)
6 - Divido valFinal por 10
7 - Somar um a contador
8 - Se val == 0 parar de repetir

9 - Multiplicar valFinal por 10 ** 3
'''

#Algoritmo Final
#Esse algoritmo exige saber a quantidade de digitos do numero
'''
0 - Obter o numero de cinco digitos, guardar em val 
    1.1 - Obter o contador, cont = quantDigito - 1)
    1.2 - Criar string vazia
Repetir 1 -> 5 enquanto val > 0:
1 - Guardar em valQuebrado = (val // 10 ** cont) Obs:Uso // para armazenar valor como int e nao float
2 - Obter algAtual = valQuebrado - (valQuebrado % 1)
3 - Atualizo val = val - (algAtual * 10 ** cont) 
4 - Atualizar cont = cont - 1
5 - Atualizar stringFinal = stringFinal + string(algAtual)

6 - Mostrar string final
'''
def main():
    val = int(input("Insira um numero inteiro de 5 digitos: "))

    stringFinal = ""
    quantiDigito = 5
    cont = quantiDigito - 1

    while val > 0:
        valQuebrado = val // 10 ** cont
        algAtual = valQuebrado - (valQuebrado % 1)
        val = val - (algAtual * (10 ** cont))
        cont -= 1
        stringFinal += f"   {str(algAtual)}"

    print(stringFinal)

if __name__ == "__main__":
    main()
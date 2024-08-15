"""
UFMT - Bacharelado em CIencia da COmputacao
Programacao de computadores
Prof. Ivairton
15/08/2024

Programa:
Leia do usuário dois operadores aritméticos entre {+, -, /, *}, faça a combinação entre os números de 1 a 3 aplicando os 
operadores informados. Por exemplo, se o usuário informar os operadores + e *, a impressão deverá obedecer ao padrão:
1 + 1 * 1 = 2
1 + 1 * 2 = 3
1 + 1 * 3 = 4
1 + 2 * 1 = 3
(…)
"""

#Meu ALgoritmo
'''
1 - Mostrar todas as possiveis combinações de formação de numero com os algarismos 1, 2 e 3
2 - Obter operacoes do usuario
2 - Operar essas possiveis combinações usando as operações escolhidas seguindo o padrão do exemplo
'''

def main():
    #Obter operacoes
    print("Escolha alguma operacao entre: {+, -, /, *}")
    op1 = input("Insira a primeira operacao")
    op2 = input("Insira a segunda operacao")

    #A partir da operacao escolhida, executar a operacao
    if op1 == "+":#SOMA
        #verifico qual a segunda operacao, opero, mostro resultado
        if op2 == "+": 
            for i in range(1, 4):
                for j in range(1, 4):
                    for k in range(1, 4):
                        print(f'{i} {op1} {j} + {k} = {i+j+k}')
        elif op2 == "-":
                for i in range(1, 4):
                    for j in range(1, 4):
                        for k in range(1, 4):
                            print(f'{i} {op1} {j} - {k} = {i+j-k}')
        elif op2 == "/":
                for i in range(1, 4):
                    for j in range(1, 4):
                        for k in range(1, 4):
                            print(f'{i} {op1} {j} / {k} = {i+j/k}')
        elif op2 == "*":
                for i in range(1, 4):
                    for j in range(1, 4):
                        for k in range(1, 4):
                            print(f'{i} {op1} {j} * {k} = {i+j*k}')
    elif op1 == "-": #SUBTRACAO
        #verifico qual a segunda operacao, opero, mostro resultado
        if op2 == "+":
            for i in range(1, 4):
                for j in range(1, 4):
                    for k in range(1, 4):
                        print(f'{i} {op1} {j} + {k} = {i-j+k}')
        elif op2 == "-":
                for i in range(1, 4):
                    for j in range(1, 4):
                        for k in range(1, 4):
                            print(f'{i} {op1} {j} - {k} = {i-j-k}')
        elif op2 == "/":
                for i in range(1, 4):
                    for j in range(1, 4):
                        for k in range(1, 4):
                            print(f'{i} {op1} {j} / {k} = {i-j/k}')
        elif op2 == "*":
                for i in range(1, 4):
                    for j in range(1, 4):
                        for k in range(1, 4):
                            print(f'{i} {op1} {j} * {k} = {i-j*k}')
    elif op1 == "/": #DIVISAO
        #verifico qual a segunda operacao, opero, mostro resultado
        if op2 == "+":
            for i in range(1, 4):
                for j in range(1, 4):
                    for k in range(1, 4):
                        print(f'{i} {op1} {j} + {k} = {i/j+k}')
        elif op2 == "-":
                for i in range(1, 4):
                    for j in range(1, 4):
                        for k in range(1, 4):
                            print(f'{i} {op1} {j} - {k} = {i/j-k}')
        elif op2 == "/":
                for i in range(1, 4):
                    for j in range(1, 4):
                        for k in range(1, 4):
                            print(f'{i} {op1} {j} / {k} = {i/j/k}')
        elif op2 == "*":
                for i in range(1, 4):
                    for j in range(1, 4):
                        for k in range(1, 4):
                            print(f'{i} {op1} {j} * {k} = {i/j*k}')
    elif op1 == "*": #MULTIPLICACAO
        #verifico qual a segunda operacao, opero, mostro resultado
        if op2 == "+":
            for i in range(1, 4):
                for j in range(1, 4):
                    for k in range(1, 4):
                        print(f'{i} {op1} {j} + {k} = {i/j+k}')
        elif op2 == "-":
                for i in range(1, 4):
                    for j in range(1, 4):
                        for k in range(1, 4):
                            print(f'{i} {op1} {j} - {k} = {i/j-k}')
        elif op2 == "/":
                for i in range(1, 4):
                    for j in range(1, 4):
                        for k in range(1, 4):
                            print(f'{i} {op1} {j} / {k} = {i/j/k}')
        elif op2 == "*":
                for i in range(1, 4):
                    for j in range(1, 4):
                        for k in range(1, 4):
                            print(f'{i} {op1} {j} * {k} = {i/j*k}')

if __name__ == "__main__":
    main()
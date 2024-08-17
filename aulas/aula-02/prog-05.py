"""
UFMT - Bacharelado em Ciencia da Computacao
Programacao de computadores
Prof. Ivairton
15/08/2024

Programa:
Imagine o contexto de um curso que irá aplicar 2 avaliações, em turmas que têm 5 alunos. 
Leia do usuário as notas das duas avaliações de cada aluno, então calcule a média de cada aluno.

Ao final, o programa deve imprimir cada nota do aluno, a sua média calculada e se ele foi aprovado (ou não), 
caso tenha média superior a 7.0.
"""

#Algoritmo
'''
1 - Obter as 10 notas, 2 para cada aluno, armazenado as notas nas listas dos respectivos alunos
2 - Calcular a media de cada aluno e guardar em uma lista separada
3 - Mostrar para cada aluno: suas notas, sua média se foi aprovado ou não (aprovado media > 7)
'''

def main():
    alunos = []
    medias = []

    print('-------CADASTRO DE NOTAS-------')
    for i in range(6):
        #Adicionando um vetor de um aluno dentro do vetor de alunos contendo a primeira nota deste aluno
        print(f'==> Aluno {i}')
        alunos.append([float(input(f'Insira a nota 0 do aluno {i}: '))])
        #Adicionando a segunda nota deste aluno no seu vetor de aluno dentro do vetor de alunos
        alunos[i].append(float(input(f'Insira a nota 1 do aluno {i}: ')))
        #Calculando e guardando as medias
        medias.append((alunos[i][0] + alunos[i][1])/2)
    
    #Mostrar para cada aluno: suas notas, sua média se foi aprovado ou não (aprovado media > 7)
    print('----------SOBRE ALUNOS----------')
    for j in range(6):
        print(f'==> Aluno {j}: ')
        print(f'Notas: {alunos[j]}')
        print(f'Media: {medias[j]}')
        if medias[j] > 7:
            print('Estado: Aprovado')
        else:
            print('Estado: Reprovado')

if __name__ == "__main__":
    main()
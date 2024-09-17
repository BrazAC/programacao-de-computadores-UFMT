"""
Aluno: Braz Amorim Campos
Data: 03/09/2024

Exercicio do notebook 5 do professor Ivairton:
- Crie um arquivo notas.txt e escreva nele os três registros a seguir, 
consistindo em IDs de alunos, nomes e notas/conceitos indicados por letras:
    1 José A
    2 Maria A
    3 Pedro B
"""

#Instanciando um objeto do tipo file no modo write e guardando em notas
notas = open('./notas2.txt', mode='w')

#Chamando o servico de manipulacao de arquivo do SO
#O with ira fechar o servico solicitado ao final da execucao do bloco interno
with notas:
    #A quebra de linha e usada para iteracoes futuras
    notas.write('1 José A\n')
    notas.write('2 Maria A\n')
    notas.write('3 Pedro B\n')


#Instanciando um objeto do tipo file no modo read e atualizando notas
notas = open('/home/braz/repos/programacao-de-computadores-UFMT/aulas/aula-files-04/questoes-notebook/notas2.txt', mode='r')

#Chamando o servico de manipulacao de arquivo do SO
with notas:
    #Iterando pelas linhas do arquivo (quebra de linha = nova linha)
    for linha in notas:
        print(linha)
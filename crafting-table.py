"""
Escreva	um	algoritmo	que	conte	de	1	até	10	e	armazene	esta	contagem	num	vetor	de	inteiros.	Mas	os	valores	devem ser	
armazenados	de	tal	forma	que	o	primeiro	valor	(1)	seja	posto	na	primeira	posiçã o	do	vetor,	o	
segundo	valor	(2)	seja	posto	na	ú ltima,	e	dessa	forma,	intercalando	entre a “ponta	esquerda” e	
a	“ponta	direita” os	valores	serã o	postos	no	vetor.	O	algoritmo	deverá	preencher	o	vetor	de	tal	
forma	que	ele	ficará	como:	 vetor[1,3,5,7,9,   10,8,6,4,2]
"""

#Algoritmo
'''
Repetir (o tamanho do vetor) = 10 vezes:
1 - Obter valor da contagem, guardar no vetor na posição alvo
    1.1 - A posicao alvo e definida alternando entre um contador crescente e um contador decrescente
          O valor do contador crescente começa em 0 e o do decrescente começa no tamanho do vetor - 1
'''

def main():
    #Criando vetor para guardar os valores
    vetor = [0] * 4
    #Obendo valor inicial do contador decrescente
    cD = len(vetor) - 1
    #Repetindo 10 vezes
    for cC in range(len(vetor)):
        #Obter valor a ser guardado
        valor = cC + 1
        #Obter a posição do vetor onde o valor será guardado nessa rodada
        if cC % 2 == 0:
            posicao = cC // 2
        else:
            posicao = cD
            cD -= 1
        #Guardando o valor na posicao obtida
        vetor[posicao] = valor
    print(vetor)

if __name__ == "__main__":
    main()
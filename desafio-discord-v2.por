/*
Escreva um algoritmo que leia valor1 e valor2 do usuário, sendo a entrada números reais positivos, com 1 casa decimal.
Calcule a média entre os dois valores. Na sequência, identifique qual dos valores informados é maior que a média, então faça uma contagem de 0 até o valor identificado.

Por exemplo, se o usuário informar para valor1 = 1.5 e valor2 = 4.2, média será 2.85. O maior valor que a média é 4.2, então o sistema deve imprimir:
0
1
2
3
4

Caso v1 == v2 imprimir que não há contagem a ser feita.

Faça também uma contagem a partir da precisão do número. 
Vamos considerar o exemplo que eu havia dado, que resultou na média 2,85, e portanto o valor dado pelo usuário que é  maior que a média era o 4,2. 
Assim, a primeira contagem foi de 0 a 4, agora faça também uma segunda contagem que vai de 0 a 2 (por conta dos 2 décimos do número de entrada).

//============PARTE 01==============================================
-Receber dois valores reais positivos com uma casa decimal de precisao
  - Impedir a entrada de valor menores que 0 (nao obrigatorio)
-Calcular a media entre os dois valores
-Identificar qual dos valores de entrada e maior que a media
-Mostrar uma contagem de 0 ate o maior valor identificado

//============PARTE 02==============================================
//NAO FUNCIONA EM PORTUGOL?
-Obter a parte fracionaria do maior valor inserido
  -modulo da divisao do maior valor por 1 <-(Isso nao funciona)
-Obter o contador alvo
  -parte fracionaria * 10 (APENAS PARA VALORES COM UMA CASA DECIMAL)
//------------
-Obter a parte inteira do maior valor inserido
  -Obter a parte fracioaria do valor
  -Subtrair a parte fracionaria do valor original
-Obter a parte fracionaria do maior valor inserido
  -Subtrair a parte inteira do valor original
-Obter o contador alvo
  -parte fracionaria * 10 (APENAS PARA VALORES COM UMA CASA DECIMAL)
*/
programa {
  funcao inicio() {
    real valorA, valorB, media, contador, maior, parteFracionaria
    inteiro parteInteira, i
    escreva("Insira o valor A: ")
    leia(valorA)
    escreva("Insira o valor B: ")
    leia(valorB)

    //Receber os valores apenas se forem >= 0
    se(valorA < 0){
      enquanto (valorA < 0){
        escreva("Insira um valor maior ou igual a 0 para A: ")
        leia(valorA)
      }
    }senao se(valorB < 0){
      enquanto (valorB < 0){
        escreva("Insira um valor maior ou igual a 0 para B: ")
        leia(valorB)
      }  
    }
    
    //Calcular a media
    media = (valorA + valorB)/2

    //Identificar qual dos valores de entrada e maior que a media
    contador = 0
    se(valorA == valorB){
      escreva("Numeros iguais portanto sem contagem")
    }senao se(valorA > media){
      //A maior que a media
      escreva("Contagem para A maior que a media: \n")
      enquanto(contador <= valorA){
        escreva(contador, "\n")
        contador += 1
        maior = valorA
      }
    }senao{
      //B maior que a media
      escreva("Contagem para B maior que a media: \n")
      enquanto(contador <= valorB){
        escreva(contador, "\n")
        contador += 1
        maior = valorB
      }
    }

    //Obtendo parte inteira do maior valor
    /*parteInteira = maior - (maior % 1)  //<-- Nao precisa fazer isso se o @ funcionar*/
    parteInteira = maior
    
    //Obtendo a parte fracionaria
    /*parteFracionaria = maior % 1  <-- @*/
    parteFracionaria = maior - parteInteira
  
    //Obtendo o contador alvo
    contador = parteFracionaria * 10 //APENAS PARA VALORES COM UMA CASA DECIMAL

    //Fazendo a segunda contagem
    escreva("Contagem para parte fracionaria: \n")
    para(i = 0; i <= contador; i++){
      escreva(i, "\n")
    }
  }
}
/*
  Receber dois valores reais positivos com uma casa decimal de precisao
    - Impedir a entrada de valor menores que 0
  Calcular a media entre os dois valores
  Identificar qual dos valores de entrada e maior que a media
  Mostrar uma contagem de 0 ate o valor identificado

*/
programa {
  funcao inicio() {
    real valorA, valorB, media, contador
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
      }
    }senao{
      //B maior que a media
      escreva("Contagem para B maior que a media: \n")
      enquanto(contador <= valorB){
        escreva(contador, "\n")
        contador += 1
      }
    }

    
  }
}

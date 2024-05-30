/*
Escreva um algoritmo que leia um valor inteiro positivo do usuário. 
Então o sistema deve “contar” de 1 até o valor informado, de modo que a cada valor contado se o valor for ı́mpar o
sistema deve imprimir o dobro do valor corrente, caso o valor seja par deverá imprimir a metade dele
*/
programa {
  funcao inicio() {
    inteiro valRef, i
    escreva("Insira um valor inteiro positivo: ")
    leia(valRef)
    para(i = 1; i <= valRef; i ++){
      se(i%2 != 0){
        escreva("O dobro do valor atual: ", i * 2,"\n")
      }senao{
        escreva("A metade do valor atual: ", i / 2,"\n")
      }
    }
  }
}

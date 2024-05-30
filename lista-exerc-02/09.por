/*
Escreva um algoritmo que leia do usuário um valor inteiro positivo de referência. Na sequencia,
leia mais 3 valores do usuário, some os 3 valores. Se o total da soma for maior que o valor de
referência o sistema deve contar de 1 até o total da soma. Caso contrário, o sistema deve contar
de 1 até o valor de referência
*/
programa {
  funcao inicio() {
    inteiro valRef, val0, val1, val2, i
    escreva("Insira um valor de referencia: ")
    leia(valRef)
    escreva("Insira o valor 01: ")
    leia(val0)
    escreva("Insira o valor 02: ")
    leia(val1)
    escreva("Insira o valor 03: ")
    leia(val2)
    se(val0+val1+val2 > valRef){
      //Contar de um ate o total da soma
      para(i=1; i<= val0+val1+val2; i++){
        escreva(i,"\n")
      }
    }senao{
      //Contar de um ate o valRef
      para(i=1; i<= valRef; i++){
        escreva(i,"\n")
      }
    }
    
  }
}

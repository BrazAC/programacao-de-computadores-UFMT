/*
 Leia um numero verifique e mostre se este e divisivel por 2, 3, 5, 10 (separadamente)
*/
programa {
  funcao inicio() {
    inteiro x
    escreva("Insira um numero: ")
    leia(x)

    se(x%2 == 0){
      escreva("Divisivel por 2")
    }senao{
      escreva("\nNao divisivel por 2")
    }

    se(x%3 == 0){
      escreva("\nDivisivel por 3")
    }senao{
      escreva("\nNao divisivel por 3")
    }

    se(x%5 == 0){
      escreva("\nDivisivel por 5")
    }senao{
      escreva("\nNao divisivel por 5")
    }

    se(x%10 == 0){
      escreva("\nDivisivel por 10")
    }senao{
      escreva("\nNao divisivel por 10")
    }

  }
}

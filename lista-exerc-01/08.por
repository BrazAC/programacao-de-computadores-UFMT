/*
Leia um numero inteiro avalie e imprima se e par ou impar
*/
programa {
  funcao inicio() {
    inteiro x
    escreva("Insira um valor inteiro: ")
    leia(x)
    se (x%2 != 0){
      escreva("Impar")
    }senao{
      escreva("Par")
    }
  }
}

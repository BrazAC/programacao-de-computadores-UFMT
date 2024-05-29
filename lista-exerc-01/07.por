programa {
  funcao inicio() {
    inteiro x
    escreva("Insira um valor inteiro: ")
    leia(x)
    se(x < 0){
      escreva("Branco")
    }senao se (x >= 0 e x <= 100){
      escreva("Verde")
    }senao se (x >= 102 e x <= 1000){
      escreva("Azul")
    }senao{
      escreva("Vermelho")
    }
  }
}

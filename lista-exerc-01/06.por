programa {
  inclua biblioteca Matematica --> mat
  funcao inicio() {
    real x
    escreva("Insira um numero real: ")
    leia(x)
    se(x >= 0){
      escreva(mat.potencia(x, (1/2)))
    }senao{
      escreva(x * x)
    }
  }
}

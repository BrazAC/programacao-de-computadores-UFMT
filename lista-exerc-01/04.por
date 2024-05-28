programa {
  inclua biblioteca Matematica --> mat
  funcao inicio() {
    real a
    escreva("Insira um numero real: ")
    leia(a)
    escreva("O numero inserido: ", a)
    escreva("\nO quadrado do numero inserido: ", a * a)
    escreva("\nRaiz quadrada do numero inserido: ", mat.potencia(a, 1/2))
  }
}

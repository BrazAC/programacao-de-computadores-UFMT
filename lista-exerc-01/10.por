//Ler dois valores inteiros, identificar qual e o maior e o menor, imprimir o maior depois o menor
programa {
  funcao inicio() {
    inteiro a, b
    escreva("Insira um valor: ")
    leia(a)
    escreva("Insira outro valor: ")
    leia(b)

    se(a < b){
      escreva(b, " e o maior valor\n")
      escreva(a, " e o menor valor\n")
    }senao{
      escreva(a, " e o maior valor\n")
      escreva(b, " e o menor valor\n")
    }
  }
}

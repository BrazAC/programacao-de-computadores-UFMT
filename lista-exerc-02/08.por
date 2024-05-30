programa {
  funcao inicio() {
    inteiro i, quatEntradas
    real valor, soma = 0
    escreva("Quantos numeros a serem somados? Escreva: ")
    leia(quatEntradas)

    para(i = 1; i <= quatEntradas; i += 1){
      escreva("Insira o valor " ,i,": ")
      leia(valor)
      soma += valor
    }

    escreva("Media dos valores: ",(soma/quatEntradas))
  }
}

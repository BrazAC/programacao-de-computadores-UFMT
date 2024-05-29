/*
Leia 2 valores inteiros do usuário, identifique o maior valor entre eles. Dobre o valor do menor
número informado pelo usuário e então verifique se ele se tornou maior que o maior valor
inicial, imprimindo o contexto obtido
*/
programa {
  funcao inicio() {
    inteiro a, b, maior, menor, menorDobrado
    escreva("Insira um valor: ")
    leia(a)
    escreva("Insira outro valor: ")
    leia(b)

    se(a < b){
      maior = b
      menor = a
    }senao{
      maior = a
      menor = b
    }

    menorDobrado = menor * 2

    se(maior < menorDobrado){
      escreva("O dobro do menor se tornou maior que o maior inicial")
    }senao{
      escreva("O dobro do menor nao se tornou maior que o maior inicial")
    }
  }
}

////Ler tres valores inteiros, identificar qual e o maior e o menor, imprimir o maior depois o menor
programa {
  funcao inicio() {
    inteiro a, b, c, menor, maior
    escreva("Insira um valor: ")
    leia(a)
    escreva("Insira outro valor: ")
    leia(b)
    escreva("Insira outro valor: ")
    leia(c)

    se(a > b e a > c){ //Caso "a" maior que todos
      maior = a
      menor = menorValor(b, c) //Determine o menor entre os menores que a
    }senao se(b > a e b > c){
      maior = b
      menor = menorValor(a, c)
    }senao{
      maior = c
      menor = menorValor(b, a)
    }
    
    escreva("Maior valor: ", maior)
    escreva("\nMenor valor: ", menor)
  }

  funcao inteiro menorValor(inteiro valA, inteiro valB){
     se(valA > valB){
      retorne valB
     }senao{
      retorne valA
     }
  }
}

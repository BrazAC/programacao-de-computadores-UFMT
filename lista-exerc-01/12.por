//Ler tres inteiros identificar e retornar o valor "do meio"
programa {
  funcao inicio() {
    inteiro a, b, c, meio
    escreva("Insira um valor: ")
    leia(a)
    escreva("Insira outro valor: ")
    leia(b)
    escreva("Insira outro valor: ")
    leia(c)

    se(a > b e a > c){ //Caso "a" maior que todos
      meio = meioValor(b, c) 
    }senao se(b > a e b > c){
      meio = meioValor(a, c)
    }senao{
      meio = meioValor(b, a)
    }
    
    escreva("Valor do meio: ", meio)
  }

  funcao inteiro meioValor(inteiro valA, inteiro valB){
     se(valA > valB){
      retorne valA
     }senao{
      retorne valB
     }
  }
  }
}

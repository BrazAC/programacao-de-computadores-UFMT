/*
Monte um sistema que ajude na decisão de um aluno. Este aluno está cursando 3 disciplinas e
já tem a nota 1 de cada uma delas. Calcule a média entre elas. Se a média for menor que 5,0, o
sistema deve sugerir que a disciplina com menor nota seja abandonada. Se a média estiver entre
5,0 e 7,0 faça um alerta, informando a menor nota que exige mais atenção
*/
programa {
  funcao inicio() {
    real a, b, c, media, menorNota, identDisciplina
    escreva("Insira a primeira nota (disciplina 1): ")
    leia(a)
    escreva("Insira a segunda nota (disciplina 2): ")
    leia(b)
    escreva("Insira a terceira nota (disciplina 3): ")
    leia(c)

    media = (a + b + c)/3

    se(a < b e a < c){ //Se nota "a" for a menor
      menorNota = a
      identDisciplina = 1
    }senao se(b < a e b < c){
      menorNota = b
      identDisciplina = 2
    }senao{
      menorNota = c
      identDisciplina = 3
    }

    se(media < 5){
      escreva("A disciplina ",identDisciplina ," com a nota de prova ", menorNota, " deve ser abandonada")
    }senao se(media >= 5 e media <= 7){
      escreva("A disciplina ",identDisciplina ," com a nota de prova ", menorNota, " deve receber mais atencao")
    }
  }
}

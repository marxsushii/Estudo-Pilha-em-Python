# Exercicio-7 (Realizado em Python)

7)<br>class Pilha {
   <br>private static int TAM_MAX = 1000;
   <br>private int valores[];
   <br>private int topo;
  <br>}
    
O código acima inicia a declaração de uma classe que implementa uma estrutura
de dados do tipo pilha. A implementação dessa pilha é baseada em vetor (valores). A
variável topo indica o topo corrente da pilha (-1 para quando a pilha está vazia). A
variável TAM_MAX contém o maior tamanho da pilha. Baseado neste código, faça:
<br>(a) Defina um construtor para a classe.
<br>(b) Altere a declaração dos campos de forma que estes não possam ser modificados
fora da classe Pilha.
<br>(c) Declare o método empty, o qual testa se uma pilha está vazia.
<br>(d) Declare o método push, o qual insere um valor no topo da pilha.
<br>(e) Declare uma variação do push, o qual permite o empilhamento de vários valores
simultaneamente.
<br>(f) Declare uma outra variação do push que permite que uma pilha inteira seja
empilhada em outra pilha.
<br>(g) Declare o método pop, o qual remove um valor do topo da pilha e o retorna.
<br>(h) Declare uma variação do método pop, a qual recebe um número e desempilha
tantos valores quanto o número passado. Caso o valor seja maior que o número
de números empilhados, todos os valores são removidos. Esta função não
retorna nenhum valor.
<br>(i) Declare o método top, o qual apenas retorna o valor do topo da pilha, sem
modificá-la.
<br>(j) Crie uma classe Principal com um método main(). Crie um objeto do tipo Pilha e
insira os valores 10, 20 e 30. Remova 2 elementos da pilha e exiba o seu topo
resultante.
<br>(k) Altere a classe para manipular objetos quaisquer, não apenas inteiros.

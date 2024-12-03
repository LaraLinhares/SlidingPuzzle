# Jogo dos Oito com Solucionador AI (BFS)

Este projeto é uma implementação simples do clássico jogo "Jogo dos Oito", que desafia o jogador a deslizar peças em uma grade 3x3 para alcançar uma configuração final. O jogo também inclui um solucionador baseado em IA que utiliza o algoritmo de Busca em Largura (BFS) para resolver automaticamente o quebra-cabeça a partir de qualquer configuração inicial.

## Funcionalidades:
- **Jogo jogável Jogo dos Oito**: Uma interface gráfica construída com `tkinter` permite que os usuários interajam com o jogo, deslizando as peças para resolver o quebra-cabeça manualmente.
- **Solucionador de IA**: O jogo inclui um solucionador de IA que utiliza o algoritmo BFS para encontrar a solução do quebra-cabeça a partir da configuração atual.
- **Geração Aleatória do Tabuleiro**: O tabuleiro começa em um estado embaralhado, garantindo que cada jogo seja único.
- **Condição de Vitória**: O jogo detecta quando o jogador resolveu o quebra-cabeça, exibindo uma mensagem de congratulações.

## Como Jogar:
1. **Iniciar o Jogo**: Ao rodar o programa, uma grade 3x3 de peças numeradas aparecerá em uma janela do tkinter. A peça vazia será representada por um espaço em branco.
2. **Deslizar as Peças**: Clique em uma peça adjacente ao espaço vazio (acima, abaixo, à esquerda ou à direita) para deslizar a peça para a posição vazia.
3. **Objetivo**: O objetivo é arranjar as peças na seguinte ordem: `1 2 3 4 5 6 7 8 0`, onde `0` representa o espaço vazio.
4. **Solucionador de IA**: Clique no botão "Resolver (BFS)" para permitir que a IA resolva o quebra-cabeça utilizando o algoritmo BFS.

## Requisitos:
- Python 3.12.3
- tkinter



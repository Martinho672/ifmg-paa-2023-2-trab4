# Relatório de Desenvolvimento - Função de Maior Substring Comum

**Fernando Martinho Nascimento & Lucas Guimarães Bernardes**

Este relatório detalha a implementação da função `biggest_substr` e destaca as dificuldades encontradas durante o desenvolvimento.

## Função `biggest_substr`

A função `biggest_substr` tem como objetivo calcular o tamanho da maior substring comum entre duas strings fornecidas como entrada. O algoritmo utilizado é baseado na programação dinâmica, preenchendo uma matriz de memória para armazenar o tamanho da substring comum para diferentes combinações de prefixos das duas strings.

### Implementação Detalhada

- Duas strings, `str1` e `str2`, são fornecidas como entrada.
- Uma matriz de memória, `mem`, é criada para armazenar os resultados intermediários dos cálculos.
- Um loop duplo itera sobre as posições da matriz, comparando as letras das duas strings.
- Se as letras comparadas são iguais, adiciona-se 1 ao valor armazenado na célula correspondente na matriz.
- Se as letras são diferentes, o valor na célula é atualizado para representar a menor string já gerada até o momento.
- A matriz é totalmente preenchida, e o valor na última célula (bottom-right) representa o tamanho da maior substring comum.

### Dificuldades de Implementação

1. **Índices fora de alcance:**
   - Um dos primeiros desafios foi garantir que os índices usados para acessar caracteres das strings e elementos da matriz de memória não ultrapassassem seus limites. Corrigir esse problema foi essencial para evitar erros de índice.

2. **Lógica de preenchimento da matriz:**
   - Compreender e implementar corretamente a lógica de preenchimento da matriz foi um desafio significativo. Especial atenção foi dada aos casos em que as letras eram iguais e diferentes, garantindo que a menor string fosse considerada.

3. **Visualização da matriz:**
   - Para depurar o código, foi útil implementar mecanismos de visualização da matriz de memória em diferentes etapas. Isso ajudou a identificar padrões e a verificar se a lógica estava funcionando conforme o esperado.

4. **Testes abrangentes:**
   - Garantir que a função funcionasse corretamente para uma variedade de casos de teste, incluindo strings vazias, foi crucial. A criação de casos de teste rigorosos ajudou a validar a robustez da implementação.

## Testes

A função `biggest_substr` foi testada com diferentes pares de strings, incluindo casos de strings idênticas, diferentes e strings vazias. Os resultados foram comparados manualmente para verificar a precisão da função.

##### Conclusão

Apesar dos desafios enfrentados, a implementação da função `biggest_substr` foi bem-sucedida, proporcionando uma compreensão mais aprofundada da programação dinâmica e suas aplicações em problemas práticos.

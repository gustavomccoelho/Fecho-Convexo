# Fecho Convexo

## Objetivo

O objetivo deste projeto é detalhar os conceitos teóricos e a abordagem prática usada para resolver o problema de definição do fecho mínimo de uma nuvem de pontos através do algoritmo “Gift Wrapping”. Assim, veremos como são feitos os cálculos para a definição dos pontos dos fechos, sua implementação em linguagem Python e uma análise da complexidade do tempo de execução de acordo com o tamanho da entrada.

## Método

A descrição teórica do método utilizado pode ser encontrada no relatório neste repositório.

## Implementação

Implementando o algoritmo em linguagem Python, e usando como entrada conjuntos de pontos pré-definidos, obtemos os seguintes resultados:

![nuvem_1](/pictures/nuvem_1.jpg)

![nuvem_2](/pictures/nuvem_2.jpg)

Também é possível implementar o algoritmo para um conjunto de pontos criados de forma aleatória, com distribuição normal. Abaixo vemos o resultado para uma nuvem de 1000 pontos:

![nuvem_3](/pictures/nuvem_3.jpg)

Abaixo podemos analisar o tempo de execução para diferentes tamanhos de entrada:

![runtime](/pictures/runtime.jpg)

## Conclusão

O algoritmo “Gift Wrapping” para identificação do fecho convexo fornece uma solução relativamente simples comparado à outros algoritmos de mesma função.  Conforme esperado, o tempo de execução do algoritmo proposto de acordo com a entrada é proporcional a〖 O〗_((nh)). Isso pode resultar em um algoritmo muito eficiente, principalmente para conjuntos com muitos pontos e poucos pontos situados no feche. É também uma boa alternativa ao algoritmo “força bruta”, que resultaria em uma complexidade〖 O〗_((n^2)). Porém, para casos especiais onde existem muitos pontos no feche, o algoritmo “Gift Wrapping” pode não ser a melhor alternativa. 

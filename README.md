
---

# Fair Scheduling

Este repositório contém o código e os scripts necessários para reproduzir os experimentos realizados no projeto de avaliação do algoritmo Completely Fair Scheduler, incluindo implementações dos algoritmos **Round Robin (RR)**, **Completely Fair Scheduler (CFS)**, **First-In, First-Out (FIFO)**, e **Shortest Job First (SJF)**.

## Geração de Carga de Processos

Para gerar uma carga de processos, utilize o script **R** `generate_data.R`. 

Neste script, o parâmetro `lambda` define a taxa de chegada dos processos ao sistema por unidade de tempo.

O parâmetro `alpha` refere-se a distribuição da duração dos processos gerados e não deve ser alterado para que os dados reflitam o comportamento de processos do UNIX.

## Simulação dos Algoritmos de Escalonamento

Para realizar a simulação dos algoritmos de escalonamento (Round Robin, CFS, FIFO, SJF), utilize o **Jupyter Notebook** `simulate.ipynb`. Nesse notebook, você pode rodar simulações para cada um dos algoritmos e visualizar os resultados.

### Como usar:

1. Gere a carga de processos com o script `generate_data.R`
2. Abra o arquivo `simulate.ipynb` no Jupyter Notebook.
3. Execute as células para obter os resultados das simulações no algoritmos desejados.
4. Gere gráficos dos resultados de turnaround time e response time com o script `plot.R`.
---

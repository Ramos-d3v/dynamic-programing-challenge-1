# GS - Dynamic Programming: Sistema de Irrigação Automatizado via SaaS 🛰️💧

**Curso:** Engenharia de Software - 2° Ano (FIAP)  
**Disciplina:**  Programação Dinâmica  

## 👥 Integrantes do Grupo
* Enzo Ramos Condomitti - RM 565832
* Murilo Mendes Marques - RM 564193
* Gabriel Carvalho Simões da Silva - RM 563169
* Gustavo Francisco Santos - RM 561820
* Gabriel Akira Borges Kiyohara - RM 565191

---

## 1. Definição do Problema 
**Cenário (Economia Espacial e Agricultura de Precisão):** Com base na análise de dados meteorológicos orbitais do nosso projeto principal, o sistema de monitoramento espacial identificou uma anomalia climática crítica: a previsão de chuvas para a próxima semana atingiu o limite inferior de risco (abaixo de 450 mm). Para mitigar o risco de perda total da safra, a plataforma central (SaaS) precisa acionar, de forma automática e imediata, a rede de irrigação artificial terrestre.

**O Problema Algorítmico:** A fazenda possui proporções continentais. O sinal de acionamento gerado pelo Servidor Central (SaaS) precisa saltar por uma extensa malha de antenas retransmissoras de rádio (IoT) até chegar à válvula de liberação de água no setor mais distante da plantação. O desafio é encontrar a **rota de comunicação com o menor tempo de latência total (em milissegundos)**, garantindo uma resposta rápida do sistema de irrigação e evitando gargalos de transmissão na rede.

---

## 2. Lógica para Resolução do Problema 
Para resolver a otimização de rotas em tempo hábil e evitar o recálculo exponencial de caminhos (força bruta), aplicamos uma combinação de três conceitos estruturais fundamentais:

1. **Grafo Direcionado Acíclico (DAG):** Modelamos a malha de comunicação IoT da fazenda como um grafo. Os "Nós" são as antenas/dispositivos (SaaS, Antena_X, Válvula) e as "Arestas" representam a conexão direcional entre eles, tendo como "peso" o tempo de latência da transmissão em milissegundos.
   
2. **Filas / Queues (`collections.deque`):** Utilizamos uma estrutura de Fila para realizar a **Ordenação Topológica** da rede. A Fila garante a integridade lógica da transmissão: uma antena só entra na fila para retransmitir o sinal adiante *depois* de ter avaliado os sinais de todas as rotas anteriores que convergem até ela.

3. **Programação Dinâmica (DP):** A lógica de Programação Dinâmica atua memorizando estados ótimos em subproblemas menores. Criamos uma memória (o dicionário `dp`) onde cada antena armazena **exclusivamente o menor tempo acumulado** para o sinal chegar até ela. 
   * **Equação de Transição:** O algoritmo verifica constantemente se: *(Tempo acumulado na Antena Atual + Latência do salto)* **<** *(Melhor tempo já conhecido do Vizinho)*. Se for verdadeiro, o vizinho atualiza a sua memória com essa nova rota mais rápida. A solução ótima na válvula final é construída através da soma dessas subsoluções ótimas locais.

---

## 3. Estruturas de Dados Utilizadas 
Conforme exigido pelo escopo da Global Solution, o algoritmo implementado em Python conta com **mais de 30 informações explícitas**. 
O Grafo (`malha_fazenda`) contém exatamente **32 nós de conexão interligados** (1 Central de Comando, 30 Antenas de Relay e 1 Válvula Setorial).

---

## 4. Como Executar o Código e Testar 

O script principal (contendo a função `def otimizar_acionamento_irrigacao`) foi desenvolvido de forma a permitir a fácil execução e interpretação do resultado final.

**Pré-requisitos:**
* Ambiente com Python 3.x instalado.

**Passo a passo:**
1. Clone este repositório no seu ambiente local.
2. Abra o terminal e navegue até a pasta do projeto.
3. Execute o script principal digitando o comando:
   ```bash
   python otimizacao_irrigacao.py
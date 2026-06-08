from collections import deque


def otimizar_acionamento_irrigacao(malha_comunicacao, origem):
    """
    Função que utiliza Fila (Topological Sort) e Programação Dinâmica
    para calcular a rota de menor latência no acionamento da irrigação.
    """

    # 1. Estrutura de DP: array de estado inicializado com infinito
    # dp[no] guarda a latência mínima acumulada para o sinal chegar àquele nó
    dp = {no: float('inf') for no in malha_comunicacao}
    dp[origem] = 0

    # 2. Mapeamento de dependências (Grau de Entrada)
    grau_entrada = {no: 0 for no in malha_comunicacao}
    for no_atual in malha_comunicacao:
        for vizinho, latencia in malha_comunicacao[no_atual]:
            grau_entrada[vizinho] += 1

    # 3. Estrutura de Dados: Fila (Queue) para organizar o processamento
    fila = deque([no for no in malha_comunicacao if grau_entrada[no] == 0])

    # 4. Resolução via Programação Dinâmica
    while fila:
        atual = fila.popleft()  # Remove o primeiro elemento da Fila

        for vizinho, latencia in malha_comunicacao[atual]:

            # Equação de Transição de Estado (Otimização)
            if dp[atual] + latencia < dp[vizinho]:
                dp[vizinho] = dp[atual] + latencia

            # Libera o vizinho. Se ele não tiver mais dependências, entra na Fila
            grau_entrada[vizinho] -= 1
            if grau_entrada[vizinho] == 0:
                fila.append(vizinho)

    return dp


# Estrutura de Grafo (Dicionário) representando a malha IoT da fazenda
# Composto por 32 nós, atendendo ao requisito da avaliação (> 30 informações)
malha_fazenda = {
    'SaaS_Central': [('Antena_1', 12), ('Antena_2', 15), ('Antena_3', 20)],
    'Antena_1': [('Antena_4', 10), ('Antena_5', 8)],
    'Antena_2': [('Antena_5', 6), ('Antena_6', 14)],
    'Antena_3': [('Antena_6', 9), ('Antena_7', 25)],
    'Antena_4': [('Antena_8', 11), ('Antena_9', 18)],
    'Antena_5': [('Antena_9', 7), ('Antena_10', 12)],
    'Antena_6': [('Antena_10', 8), ('Antena_11', 15)],
    'Antena_7': [('Antena_11', 5), ('Antena_12', 20)],
    'Antena_8': [('Antena_13', 14)],
    'Antena_9': [('Antena_13', 9), ('Antena_14', 11)],
    'Antena_10': [('Antena_14', 6), ('Antena_15', 10)],
    'Antena_11': [('Antena_15', 8), ('Antena_16', 13)],
    'Antena_12': [('Antena_16', 12)],
    'Antena_13': [('Antena_17', 22)],
    'Antena_14': [('Antena_17', 14), ('Antena_18', 9)],
    'Antena_15': [('Antena_18', 11), ('Antena_19', 15)],
    'Antena_16': [('Antena_19', 7)],
    'Antena_17': [('Antena_20', 10)],
    'Antena_18': [('Antena_20', 12), ('Antena_21', 9)],
    'Antena_19': [('Antena_21', 8), ('Antena_22', 16)],
    'Antena_20': [('Antena_23', 7)],
    'Antena_21': [('Antena_23', 11), ('Antena_24', 14)],
    'Antena_22': [('Antena_24', 10)],
    'Antena_23': [('Antena_25', 18)],
    'Antena_24': [('Antena_25', 13), ('Antena_26', 12)],
    'Antena_25': [('Antena_27', 8)],
    'Antena_26': [('Antena_27', 10), ('Antena_28', 15)],
    'Antena_27': [('Antena_29', 14)],
    'Antena_28': [('Antena_29', 9), ('Antena_30', 11)],
    'Antena_29': [('Valvula_Setor_Critico', 13)],
    'Antena_30': [('Valvula_Setor_Critico', 6)],
    'Valvula_Setor_Critico': []
}

if __name__ == "__main__":
    latencia_final = otimizar_acionamento_irrigacao(malha_fazenda, 'SaaS_Central')
    print(f"📡 Anomalia climática detectada (chuvas < 450mm).")
    print(f"💧 Acionando irrigação. Tempo mínimo de resposta da rede: {latencia_final['Valvula_Setor_Critico']} ms.")
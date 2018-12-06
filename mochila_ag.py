import random

# Geração da população inicial
def gera_populacao():
    populacao = []
    i = 0
    while (i < tamanho):
        j = 0
        individuo = []
        while (j < objetos):
            item = random.randint(0, 1)
            individuo.append(item)
            j += 1
        if individuo not in populacao:
            populacao.append(individuo)
            i += 1
    return populacao

# Avaliação da população
def avalia_populacao(populacao):
    avaliacao = []
    for i in range(len(populacao)):
        somavalores = 0
        for j in range(objetos):
            if(populacao[i][j] == 1):
                somavalores += valores[j]
        avaliacao.append(somavalores)
    return avaliacao

# Ordenação da população
def ordena_populacao(avaliacao, populacao):
    avaliacao_ordenada = sorted(avaliacao)
    populacao_ordenada = []
    i = len(avaliacao_ordenada)-1
    while (i >= 0):
        maior = avaliacao_ordenada[i]
        indice_maior = avaliacao.index(maior)
        populacao_ordenada.append(populacao[indice_maior])
        i -= 1
    populacao_ordenada.reverse()
    return avaliacao_ordenada, populacao_ordenada

# Seleção dos casais
def selecao_casais(avaliacao, populacao):
    casais = []
    while len(populacao) > 0:     # taxa de reprodução = 100%
        indice = roleta_reproducao(avaliacao, populacao)
        casais.append(populacao[indice])
        del(populacao[indice])
        del(avaliacao[indice])
    return casais

# Método da roleta
def roleta_reproducao(avaliacao, populacao):
    total = sum(avaliacao)
    roleta = []
    for j in range(len(avaliacao)):
        if j == 0:
            roleta.append(avaliacao[j])
        else:
            roleta.append(roleta[j-1] + avaliacao[j])
    parent = random.randint(0, total)
    k = 0
    while (parent > roleta[k]):
        k += 1
    return k

# Recombinação Genética / Crossover
def recombinacao(casais):
    filhos = []
    for i in range(1,len(casais),2):
        pai = casais[i-1]
        mae = casais[i]
        ponto_corte = random.randint(0, objetos-1)
        # Filho (1º descendente)
        filho_p = pai[0:ponto_corte] 
        filho_m = mae[ponto_corte:len(mae)]
        filho = filho_p + filho_m
        # Filha (2º descendente)
        filha_m = mae[0:ponto_corte]
        filha_p = pai[ponto_corte:len(mae)]
        filha = filha_m + filha_p
        # Salvando os filhos
        filhos.append(filho)
        filhos.append(filha)
    return filhos

# Mutação Genética
def mutacao(filhos):
    for i in range(len(filhos)):
        x = random.randint(0, 100)
        if(x <= taxa_mutacao):
            k = random.randint(0, objetos-1)
            if (filhos[i][k] == 1):
                filhos[i][k] = 0
            else:
                filhos[i][k] = 1

# Ajuste populacional
def nova_geracao(filhos):
    nova_populacao = []
    nova_populacao = filhos
    return nova_populacao

# Calcula pesos de uma população
def calcula_pesos(populacao):
    pesospopulacao = []
    for i in range(len(populacao)):
        somapesos = 0
        for j in range(objetos):
            if(populacao[i][j] == 1):
                somapesos += pesos[j]
        pesospopulacao.append(somapesos)
    return pesospopulacao

# Solução ótima
def solucao_otima(populacao):
    avaliacao_np = avalia_populacao(populacao)
    pesos_np = calcula_pesos(populacao)
    for i in range(len(populacao)):
        if pesos_np[i] > capacidade:
            del(pesos_np[i])
            del(avaliacao_np[i])
            del(populacao[i])
    melhor = max(avaliacao_np)
    indice_melhor = avaliacao_np.index(melhor)
    peso_melhor = pesos_np[indice_melhor]
    individuo_melhor = populacao[indice_melhor]
    return melhor, peso_melhor, individuo_melhor

def algoritmo_genetico(populacao, iteracoes):
    iteracao = 1
    while iteracao < iteracoes:

        # Etapa 1: Avaliação da população
        avaliacao = avalia_populacao(populacao)
        print(avaliacao)

        # Etapa 2: Ordenação da população
        avaliacao_ordenada, populacao_ordenada = ordena_populacao(avaliacao.copy(), populacao)
        print(avaliacao_ordenada)
        print(populacao_ordenada)

        # Etapa 3: Seleção dos casais
        casais = selecao_casais(avaliacao_ordenada.copy(), populacao_ordenada.copy())
        print(casais)

        # Etapa 4: Recombinação genética
        filhos = recombinacao(casais)
        print(filhos)

        # Etapa 5: Mutação
        mutacao(filhos)
        print(filhos)

        # Etapa 6: Ajuste populacional
        nova_populacao = nova_geracao(filhos)
        populacao = nova_populacao
    
        iteracao += 1

    return populacao


if __name__== "__main__":

    ''' 
    Inicializando variáveis
    '''
    capacidade = int(200)          # Capacidade da mochila
    pesos = [5, 10, 15, 20, 25]    # Pesos dos objetos, em ordem
    valores = [8, 16, 64, 20, 52]  # Valores dos objetos, em ordem
    objetos = int(5)               # Quantidade de objetos disponíveis
    tamanho = int(6)               # Tamanho da população
    taxa_mutacao = int(5)          # Probabilidade (%) de um indivíduo sofrer mutação em algum de seus genes

    '''
    Execução do Algoritmo Genético - Aplicado ao Problema da Mochila
    '''

    # Etapa 0: Geração da população inicial
    populacao = gera_populacao()
    print(populacao)

    populacao_final = algoritmo_genetico(populacao, 5)  # 5 == quantidade de iterações
    print(populacao_final)

    # Etapa 7: Escolhe a solução ótima na população final que não viola a restrição de capacidade
    avaliacao_op, peso_op, individuo_op = solucao_otima(populacao_final)
    print("Nota da solução ótima: ", avaliacao_op)
    print("Peso da solução ótima: ", peso_op)
    print("Melhor indivíduo: ", individuo_op)
    





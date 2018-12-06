import random

# Inicializando variáveis -- 1
c = int(200)
p = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
v = [8, 16, 64, 20, 52, 46, 2, 18, 32, 10]
elementos = list(range(0, 10))

# Inicializando variáveis -- 2
matrizResult = []
pResult = []
vResult = []
somaPesos = 0
somaValores = 0

# Quantidade máxima de objetos para escolher dentro do conjunto
k = int(input("Defina a quantidade de objetos para colocar na mochila: "))

# Calcula o total do Valor e do Peso para os objetos selecionados a cada iteração
for i in range(100):
    escolhidos = random.sample(elementos, k)
    matrizResult.append(escolhidos)
    for j in escolhidos:
        somaPesos += p[j]
        somaValores += v[j]
    pResult.append(somaPesos)
    vResult.append(somaValores)

# Elimina as soluções que não satisfazem à restrição da capacidade da mochila
for a in pResult:
    if a > c:
        indexPeso = pResult.index(a)
        pResult[indexPeso] = -1
        vResult[indexPeso] = -1

# Seleciona a solução de maior Valor
maiorValor = max(vResult)
indexMaiorValor = vResult.index(maiorValor)

# Encontra o peso e os objetos correspondentes à solução de maior valor
print('Valor: ', maiorValor)
print('Peso: ', pResult[indexMaiorValor])
print('Objetos', matrizResult[indexMaiorValor])

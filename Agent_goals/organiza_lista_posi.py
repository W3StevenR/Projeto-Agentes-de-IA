

# Função para calcular a distância euclidiana entre dois pontos
def distancia_entre_pontos(ponto1, ponto2):
    return ((ponto1[0] - ponto2[0]) ** 2 + (ponto1[1] - ponto2[1]) ** 2) ** 0.5

# Função para encontrar o ponto mais próximo não visitado
def encontrar_proximo_ponto(posicao_atual, pontos_restantes):
    menor_distancia = float('inf')
    ponto_mais_proximo = None
    for ponto in pontos_restantes:
        distancia = distancia_entre_pontos(posicao_atual, ponto)
        if distancia < menor_distancia:
            menor_distancia = distancia
            ponto_mais_proximo = ponto
    return ponto_mais_proximo

# Função para encontrar a ordem de visita dos pontos
def encontrar_ordem_visita(coordenadas):
    ordem_visita = []
    pontos_restantes = list(coordenadas)
    posicao_atual = pontos_restantes.pop(0)  # Começar no primeiro ponto
    ordem_visita.append(posicao_atual)
    while pontos_restantes:
        proximo_ponto = encontrar_proximo_ponto(posicao_atual, pontos_restantes)
        ordem_visita.append(proximo_ponto)
        pontos_restantes.remove(proximo_ponto)
        posicao_atual = proximo_ponto
      
    print("Ordem de visita dos pontos:", ordem_visita)
    return ordem_visita
    





# Encontrar a ordem de visita dos pontos
#ordem_visita = encontrar_ordem_visita(coordenadas)

# Imprimir a ordem de visita dos pontos
   

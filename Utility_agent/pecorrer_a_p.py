def percorrer_matriz_por_ordem_com_caminho(environment, ordem):
  posicao_atual = ordem[0]  # Começar na posição inicial da matriz
  lista_direcao = []
  for ponto in ordem:
      x, y = ponto
  
      while posicao_atual != ponto:
          direcao = '' 
          x_atual, y_atual = posicao_atual
          if x_atual < x:
              x_atual += 1
              direcao = 'Down'
          elif x_atual > x:
              x_atual -= 1
              direcao = 'Up'
          elif y_atual < y:
              y_atual += 1
              direcao = 'Right'
          elif y_atual > y:
              y_atual -= 1
              direcao = 'Left'
  
          posicao_atual = (x_atual, y_atual)
  
          lista_direcao.append(direcao)
          print(f'Movimento: {direcao}, posição atual: {posicao_atual}, valor: {environment[x_atual][y_atual]}')
  return lista_direcao



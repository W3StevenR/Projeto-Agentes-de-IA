import random
import time
import organiza_lista_posi
import pecorrer_a_p


class UtilityBasedModel:
  
  def __init__(self):
    self.position = (1, 1)
    self.points = 0
    self.item = 'nada'
    self.list_O = []
    self.list_X = []
    self.lista_principal = []
    self.retorno = []
    self.rota_agente = []
    self.environment = self.create_environment()
    self.start_time_objt = time.time()  # Tempo inicial

  def create_environment(self):

    # Cria o Ambiente 20x10 preenchido com '-'
    environment = [['-' for _ in range(20)] for _ in range(20)]
    # Faz 5 loops para adc os itens na lista
    # Gera coordenas aleatorias para x,y e verifica se ja há item nessa posição
    # o append guarda as coordenas do item no mapa para uso futuro

    for _ in range(5):
      x, y = random.randint(1, 19), random.randint(1, 19)
      while environment[x][y] != '-':
        x, y = random.randint(1, 19), random.randint(1, 19)
      environment[x][y] = 'O'
      self.list_O.append((x, y))

    # Similia com X
    for _ in range(5):
      x, y = random.randint(1, 19), random.randint(1, 19)
      while environment[x][y] != '-':
        x, y = random.randint(1, 19), random.randint(1, 19)
      environment[x][y] = 'X'
      self.list_X.append((x, y))

    # Lista principal vai conter as coordenadas de todos os itens JUNTOS em lista separadas, ajudará a calcular a melhor rota de visita para cada TIPO de item separadamente
    self.lista_principal = [self.list_O, self.list_X]
    print('lista p', self.lista_principal)
    return environment

  # Nesta função vai ser responsavel pelo reconhecimento dos objetivos dando a melhor rota de visita ponderando o peso entre X e O e retornando o comando de ações com o caminho
  def acoes_pre_estabelicidas(self):
    coordenada = [(1, 1)]  # vai ser a ordem dos pontos de visita

    for lista in self.lista_principal:
      print("primeira ", lista)
      coordenada.extend(organiza_lista_posi.encontrar_ordem_visita(lista))
    self.rota_agente.extend(
        pecorrer_a_p.percorrer_matriz_por_ordem_com_caminho(
            self.environment, coordenada))

  def percept(self):
    x, y = self.position
    print(f"Percept: Agent at position ({x}, {y})")
    return self.environment[x][y]

  def act(self, percept):
    if percept == 'X':
      self.points += 10
      self.item = 'com'
      return 'Pegar'

    elif percept == 'O':
      self.points += 20
      self.item = 'com'
      return 'Pegar'

    elif self.position == (
        1, 1
    ) and self.item == 'com':  # Nesta codição quando o agente faz o retorno apos capturar todos os itens, aciona a opção largar
      return 'Larga'

    else:
      # Neste trecho ele verifica se a rota de ações esta vazia e recalcula a rota de retorno da posição atual
      if not self.rota_agente:
        self.rota_agente = pecorrer_a_p.percorrer_matriz_por_ordem_com_caminho(
            self.environment, [self.position, (1, 1)])

      else:
        # Neste trecho aciona o andar do agente pois na posição atual não tera uma ação
        aux = self.rota_agente[0]
        # print(aux)
        self.rota_agente.pop(0)

        return aux

  def update_position(self, action):

    if action == 'Left':
      self.position = (self.position[0], max(1, self.position[1] - 1))

    elif action == 'Right':
      self.position = (self.position[0], min(20, self.position[1] + 1))

    elif action == 'Up':
      self.position = (max(1, self.position[0] - 1), self.position[1])

    elif action == 'Down':

      self.position = (min(20, self.position[0] + 1), self.position[1])
    elif action == 'Larga':
      self.item = 'Nenhum'

    elif action == 'Pegar':
      a, b = self.position
      self.environment[a][b] = '-'

  def main(self):
    print("Initial Environment:")
    self.acoes_pre_estabelicidas()
    self.print_environment()
    print(self.rota_agente)

    for lista in self.lista_principal:
      while 'X' in [item for sublist in self.environment for item in sublist] or \
              'O' in [item for sublist in self.environment for item in sublist] or self.item == 'com':
        percept = self.percept()
        action = self.act(percept)
        self.update_position(action)
        if action == 'Pegar':
          

          print("\nAgent's action:", action)
          print("Environment after agent's action:")
        self.print_environment()
        print("Posse de item: ", self.item)

    # Calcula a medida de desempenho
    end_time = time.time()  # Tempo final
    elapsed_time = end_time - self.start_time_objt  # Tempo decorrido
    measure_of_performance = elapsed_time + self.points
    print("\nMeasure of performance:", measure_of_performance)

    print("\nTotal points:", self.points)

  def print_environment(self):
    for i in range(0, 20):
      for j in range(0, 20):
        if (i, j) == self.position:
          print('A', end=' ')
        else:
          print(self.environment[i][j], end=' ')
      print()
    # time.sleep(1)


if __name__ == "__main__":
  agent = UtilityBasedModel()
  agent.main()

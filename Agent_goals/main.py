import random
import time
import organiza_lista_posi
import pecorrer_a_p


class GoalBasedAgent:

  def __init__(self):
    self.position = (1, 1)
    self.points = 0
    self.item = 'nada'
    self.list = [(1, 1)]
    self.retorno = []
    self.rota_agente = []
    self.environment = self.create_environment()
    self.visited_positions = [
    ]  # Lista para armazenar as posições visitadas com item
    self.last_state = None  # Variável para armazenar o estado anterior
    self.start_time_objt = time.time()  # Tempo inicial

  def create_environment(self):
    environment = [['-' for _ in range(20)] for _ in range(20)]
    for _ in range(5):
      x, y = random.randint(1, 19), random.randint(1, 19)
      while environment[x][y] != '-':
        x, y = random.randint(1, 19), random.randint(1, 19)
      environment[x][y] = 'X'
      self.list.append((x, y))
    for _ in range(5):
      x, y = random.randint(1, 19), random.randint(1, 19)
      while environment[x][y] != '-':
        x, y = random.randint(1, 19), random.randint(1, 19)
      environment[x][y] = 'O'
      self.list.append((x, y))
    return environment

  def acoes_pre_estabelicidas(self):
    self.list = organiza_lista_posi.encontrar_ordem_visita(self.list)

    self.rota_agente = pecorrer_a_p.percorrer_matriz_por_ordem_com_caminho(
        self.environment, self.list)

  def percept(self):
    x, y = self.position
    print(f"Percept: Agent at position ({x}, {y})")
    return self.environment[x][y]

  def act(self, percept):
    if percept == 'X':
      self.points += 10
      self.item = 'com'
      self.visited_positions.append(
          self.position)  # Adiciona a posição atual à lista de visitadas
      return 'Pick'
    elif percept == 'O':
      self.points += 20
      self.item = 'com'
      self.visited_positions.append(
          self.position)  # Adiciona a posição atual à lista de visitadas
      return 'Pick'
    elif self.position == (1, 1) and self.item == 'com':
      print('´pja')
      return 'Larga'

    else:

      if not self.rota_agente:
        self.rota_agente = pecorrer_a_p.percorrer_matriz_por_ordem_com_caminho(
            self.environment, [self.position, (1, 1)])

      else:
        aux = self.rota_agente[0]
        #print(aux)
        self.rota_agente.pop(0)

        return aux

  def update_position(self, action):

    if action == 'Left':
      self.last_state = self.position
      self.position = (self.position[0], max(1, self.position[1] - 1))

    elif action == 'Right':
      self.last_state = self.position
      self.position = (self.position[0], min(20, self.position[1] + 1))

    elif action == 'Up':
      self.last_state = self.position
      self.position = (max(1, self.position[0] - 1), self.position[1])

    elif action == 'Down':

      self.last_state = self.position
      self.position = (min(20, self.position[0] + 1), self.position[1])
    elif action == 'Larga':
      self.item = 'Nenhum'

  def run(self):
    print("Initial Environment:")
    self.acoes_pre_estabelicidas()
    self.print_environment()
    print(self.rota_agente)

    while 'X' in [item for sublist in self.environment for item in sublist] or \
            'O' in [item for sublist in self.environment for item in sublist] or self.item=='com':
      percept = self.percept()
      action = self.act(percept)
      self.update_position(action)
      if action == 'Pick':
        a, b = self.position
        self.environment[a][b] = '-'

      print("\nAgent's action:", action)
      print("Ambiente depois da ação do agente:")
      self.print_environment()
    print("Posse de item: ", self.item)

    
    # Calcula a medida de desempenho
    end_time = time.time()  # Tempo final
    elapsed_time = end_time - self.start_time_objt  # Tempo decorrido
    measure_of_performance = elapsed_time + self.points
    print("\nPerformace:", measure_of_performance)

    print("\nPontos totais:", self.points)

    print("Posições visitadas com itens:", self.visited_positions)

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
  agent = GoalBasedAgent()
  agent.run()

import random
import time
import pecorrer_a_p
import os


class ModelBasedAgent:

  def __init__(self):
    self.position = (1, 1)
    self.points = 0
    self.item = 'nada'
    self.visited_positions = [
    ]  # Lista para armazenar as posições visitadas com item
    self.last_state = None  # Variável para armazenar o estado anterior
    self.start_time_objt = time.time()  # Tempo inicial
    self.rota_retorno = []

  def percept(self, environment):
    x, y = self.position
    print(f"Percept: Agent at position ({x}, {y})")
    return environment[x][y]

  def act(self, percept):
    if percept == 'X':
      self.points += 10
      self.item = 'com'
      self.visited_positions.append(self.position)
      return 'Pegar'
    elif percept == 'O':
      self.points += 20
      self.item = 'com'
      self.visited_positions.append(self.position)
      return 'Pegar'
    elif self.position == (1, 1) and self.item == 'com':
      return 'Largar'
    else:
      return random.choice(['Left', 'Right', 'Up', 'Down', 'NoOp'])

  def update_position(self, action, environment):
    if action == 'Left':
      if (self.position[0], max(
          1, self.position[1] - 1)) in self.visited_positions or (
              self.position[0], max(1,
                                    self.position[1] - 1)) == self.last_state:
        action = random.choice(['Left', 'Right', 'Up', 'Down', 'NoOp'])
        self.update_position(action,environment)
      else:
        self.last_state = self.position
        self.position = (self.position[0], max(1, self.position[1] - 1))
    elif action == 'Right':
      if (self.position[0], min(
          20, self.position[1] + 1)) in self.visited_positions or (
              self.position[0], min(20,
                                    self.position[1] + 1)) == self.last_state:
        action = random.choice(['Left', 'Right', 'Up', 'Down', 'NoOp'])
        self.update_position(action,environment)
      else:
        self.last_state = self.position
        self.position = (self.position[0], min(20, self.position[1] + 1))
    elif action == 'Up':
      if (max(1, self.position[0] - 1),
          self.position[1]) in self.visited_positions or (max(
              1, self.position[0] - 1), self.position[1]) == self.last_state:
        action = random.choice(['Left', 'Right', 'Up', 'Down', 'NoOp'])
        self.update_position(action,environment)
      else:
        self.last_state = self.position
        self.position = (max(1, self.position[0] - 1), self.position[1])
    elif action == 'Down':
      if (min(20, self.position[0] + 1),
          self.position[1]) in self.visited_positions or (min(
              20, self.position[0] + 1), self.position[1]) == self.last_state:
        action = random.choice(['Left', 'Right', 'Up', 'Down', 'NoOp'])
        self.update_position(action,environment)
      else:
        self.last_state = self.position
        self.position = (min(20, self.position[0] + 1), self.position[1])
    elif action == 'Largar':
      self.item = 'Nada'
      action = random.choice(['Left', 'Right', 'Up', 'Down', 'NoOp'])
      self.update_position(action,environment)

    elif action == 'Pegar':
      a, b = self.position
      environment[a][b] = '-'


def create_environment():
  environment = [[' ' for _ in range(21)] for _ in range(21)]
  for _ in range(5):
    x, y = random.randint(1, 20), random.randint(1, 20)
    while environment[x][y] != ' ':
      x, y = random.randint(1, 20), random.randint(1, 20)
    environment[x][y] = 'X'

  for _ in range(5):
    x, y = random.randint(1, 20), random.randint(1, 20)
    while environment[x][y] != ' ':
      x, y = random.randint(1, 20), random.randint(1, 20)
    environment[x][y] = 'O'

  return environment


def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')


def print_environment(environment, agent):
  clear_screen()
  for i in range(1, 21):
    for j in range(1, 21):
      if (i, j) == agent.position:
        print('A', end=' ')
      else:
        print(environment[i][j], end=' ')
    print()
  # time.sleep(0.05)


def retorno(self, environment):
  self.rota_retorno = pecorrer_a_p.percorrer_matriz_por_ordem_com_caminho(
      environment, [self.position, (1, 1)])


def main():
  environment = create_environment()
  agent = ModelBasedAgent()

  print("Ambiente Inicial:")
  print_environment(environment, agent)

  while 'X' in [item for sublist in environment for item in sublist] or \
        'O' in [item for sublist in environment for item in sublist] or agent.item == 'com':
    percept = agent.percept(environment)
    action = agent.act(percept)
    agent.update_position(action,environment)

    if action == 'Pegar':

      retorno(agent, environment)

      for acao in agent.rota_retorno:
        agent.update_position(acao,environment)

        print("\nAgent's action:", acao)
        print("Ambiente depois da ação do agente:")
        print_environment(environment, agent)
        print('Posse de item: ', agent.item)
        # time.sleep(1)

    print("\nAgent's action:", action)
    print("Ambiente depois da ação do agente:")
    print_environment(environment, agent)
    print(agent.item)

  # Calcula a medida de desempenho
  end_time = time.time()  # Tempo final
  elapsed_time = end_time - agent.start_time_objt  # Tempo decorrido
  measure_of_performance = elapsed_time + agent.points
  print("\nPerformace:", measure_of_performance)

  print("\nPontos totais:", agent.points)
  print("Posições visitadas com itens:", agent.visited_positions)


if __name__ == "__main__":
  main()

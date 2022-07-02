"""
Текущее базовое решение (02.07.2022) 
"""

import ga_functions as gen_algf
import graph_functions as gf


class GA():
  """
  Класс, реализующий инициализацию
  и запуск генетического алгоритма.
  """

  def __init__(self, num_of_individuals, selection_coefficient, \
               probability_of_mutation, gens_mutation, \
               num_of_generations, log_cycle, graph, reproduction, \
               mutations, selection, fitness):
    """
    ------Параметры------
    num_of_individuals - количество особей в популяции. В текущей
    версии это число фиксировано.

    selection_coefficient - количество "элитарных" особей
    
    probability_of_mutation - вероятность мутации особи
    
    gens_mutation - вероятность мутации гена
    nums_of_generations - количество генераций алгоритма
    
    log_cycle - частота вывода логов в количестве
    генераций (например, значение 3 означает, что информация
    о популяции будет выводиться один раз в три генерации)

    graph - граф, минимальное остовное дерево которого надо найти

    reproduction, mutations, selection, fitness - функции кроссовера,
    мутации, отбора и фитнеса.
    """

    self.num_of_individuals = num_of_individuals
    self.selection_coefficient = selection_coefficient
    self.probability_of_mutation = probability_of_mutation
    self.gens_mutation = gens_mutation
    self.num_of_generations = num_of_generations
    self.log_cycle = log_cycle
    self.graph = graph
    self.reproduction = reproduction
    self.mutations = mutations
    self.selection = selection
    self.fitness = fitness
    self.num_of_edges = gf.get_number_of_edges(graph)

  def run(self):
    individuals = gen_algf.create_individuals(self.num_of_edges, self.num_of_individuals)
    gen_algf.assign_fitness(individuals, self.graph, self.fitness)
    for generation in range(1, self.num_of_generations+1):
      # логирование
      if generation % self.log_cycle == 0:
        gen_algf.log(individuals, generation)

      # запуск кроссовера
      new_individuals = self.reproduction(individuals, self.num_of_edges)
      gen_algf.assign_fitness(individuals, self.graph, self.fitness)
      
      # объединение потомков с родителями и произведение мутаций
      individuals += new_individuals
      self.mutations(individuals, self.probability_of_mutation, \
                     self.gens_mutation, self.num_of_edges)
      gen_algf.assign_fitness(individuals, self.graph, self.fitness)
      
      # отбор особей в новую популяцию
      individuals = self.selection(individuals, self.num_of_individuals,\
                                   self.selection_coefficient)


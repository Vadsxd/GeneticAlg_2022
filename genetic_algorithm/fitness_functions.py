"""
Данный файл содержит различные фитнес-функции.

------Соглашение о реализуемых фитнес-функциях------
Фитнес-функция не должна быть меньше либо равна 0. Это
условие создано для комфортного использования функции
random.choices в функциях отбора.

"""

from graph_functions import individual_to_graph, tree_cost


def fitness_function(individual, init_graph, epsilon=0.001):
  """
  Фитнес функция, вычисляющая значение по 
  следующему принципу:
  -- если гентический код особи представляет не дерево,
  то возвращается малое значение (epsilon)
  -- в противном случае возвращается величина
  1 / вес дерева 

  ------Параметры------
  individual - особь
  init_graph - граф
  epsilon - малое положительное значение
  """
  graph = individual_to_graph(individual.gen_code, init_graph)
  answer =  1 / tree_cost(graph)
  if answer == 0:
    answer += epsilon
  return answer




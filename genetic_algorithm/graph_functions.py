"""
В данном файле представлены все функции
для работы с графами.

------Соглашение о представлении графов------
Неориентированный граф представлен с помощью списка 
смежности следующим образом:
графом является список списков. В списке с индексом
i хранятся все ребра, инцидентные вершине i в виде
(вес, <номер вершины, инцидентной вершине i>)

"""

import random
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree


def create_full_graph(n, a=1, b=25):
  """
  Создает полный граф на n вершинах со 
  случайными весами.

  ------Параметры------
  n - количество вершин
  a - достижимая нижняя граница веса ребра
  b - дотижимая верхняя граница веса ребра
  """
  return [[(random.randint(a, b), j) for j in list(range(i)) + list(range(i+1, n))] for i in range(n)]


def individual_to_graph(individual_code, init_graph):
  """
  Конвертирует генетический код особи в представляемый
  им граф.

  ------Параметры------
  individual_code - генетический код
  init_graph - граф, на основе которого сгенерирован
  генетический код
  """
  n = len(init_graph)
  graph = [[] for i in range(n)]
  mask = 1
  for source in range(n):
    for weight, destination in init_graph[source]:
      # так как граф двунаправленный, представление
      # некоторых ребер повторяется
      if source > destination:
        continue
      
      if individual_code & mask: # это ребро присутствует
        graph[source].append((weight, destination))
        graph[destination].append((weight, source))
      
      mask = mask << 1 # переход к проверке следующего ребра
  return graph

def tree_cost(tree):
  """
  Оценивает вес остовного дерева. Если
  переданный граф не является остовным 
  деревом, то его вес равняется бесконечности.
  """

  # количество вершин
  n = len(tree)

  is_visited = [False] * n
  num_edges = get_number_of_edges(tree)
  visited_edges = 0
  cost, visited_edges = depth_search(tree, 0, is_visited, 0, visited_edges)

  # если в результате поиска в глубину не были посещены
  # какие-либо вершины или ребра, то граф не является 
  # деревом
  if False in is_visited or visited_edges != num_edges:
    cost = float("Inf")
  return cost

def depth_search(graph, start, is_visited, cost, visited_edges):
  """
  Функция реализует поиск в глубину с учетом 
  посещенный вершин, количества посещенный ребер 
  и их суммарного веса.

  ------Параметры------
  graph - граф
  start - номер начальной вершины
  is_visited - булевый список посещенных вершин
  cost - вес дерева обхода
  visited_edges - количество посещенных ребер
  """
  is_visited[start] = True
  for weight, destination in graph[start]:
    if is_visited[destination]:
      continue
    cost += weight
    visited_edges += 1
    cost, visited_edges = depth_search(graph, destination, is_visited, cost, visited_edges)
  return cost, visited_edges

def list_to_adjacency_matrix(graph):
  """
  Конвертирует представление графа из списка
  в матрицу смежности, что может 
  понадобиться для работы с функциями из
  skipy.
  """
  n = len(graph)
  matrix = [[0] * n for i in range(n)]
  for source in range(n):
    for weight, destination in graph[source]:
      if destination < source:
        continue
      matrix[source][destination] = weight
  return matrix

def matrix_to_adjacency_list(graph):
  """
  Конвертирует представление графа из матрицы
  смежности в список, что может 
  понадобиться для работы с функциями из
  skipy.
  """
  n = len(graph)
  adjacency_list = [[] for i in range(n)]
  for i in range(n):
    for j in range(n):
      if graph[i][j]:
        adjacency_list[i].append((graph[i][j], j))
        adjacency_list[j].append((graph[i][j], i))
  return adjacency_list


def weight_of_min_tree(graph):
  """
  Возвращает вес минимального остовного
  дерева.
  """
  n = len(graph)
  matrix = list_to_adjacency_matrix(graph)
  matrix = csr_matrix(matrix)
  min_tree = minimum_spanning_tree(matrix)
  min_tree = min_tree.toarray().astype(int)
  return np.sum(np.sum(min_tree, axis=0), axis=0)

def get_number_of_edges(graph):
  """
  Выдает количество ребер в графе.
  """
  answer = 0
  for i in range(len(graph)):
    answer += len(graph[i])
  # каждое ребро представлено в графе дважды
  return answer // 2





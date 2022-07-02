"""
Данный файл содержит функции кроссовера.

------Соглашение о реализуемых функциях кроссовера------
Функция кроссовера должна выдавать на выход список созданных особей.
"""

from individual import Individual
import random


def uniform_reproduction(individuals, num_of_gens):
  """
  Функция, генерирующая новых особей с помощью
  однородного кроссовера с выбором родителей по принципу рулетки. 
  Возвращает список новых особей, длина которого равна длине переданного
  списка особей, который будет использоваться для выбора
  родителей.

  ------Параметры------
  individuals - список родителей
  num_of_gens - длина генетического кода (количество ребер в графе)
  """

  num_of_indiv = len(individuals)
  
  new_individuals = [] # список новых особей

  # вероятность выбора особи в качестве родителя прямо 
  # пропорциональна значению фитнес-функции
  weights = [individual.fitness for individual in individuals]

  ones = int(2 ** num_of_gens - 1) # единичная маска

  # два родителя генерируют двух потомков
  for i in range(num_of_indiv // 2): 
    x, y = random.choices(individuals, weights, k=2)
    mask = random.randint(1, 2 ** (num_of_gens - 1))
    first, second = x.gen_code & mask + (mask ^ ones) & y.gen_code, \
    y.gen_code & mask + (mask ^ ones) & x.gen_code
    new_individuals.append(Individual(first))
    new_individuals.append(Individual(second))
  return new_individuals



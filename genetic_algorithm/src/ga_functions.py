"""
Данный файл содержит вспомогательные функции
для генетического алгоритма.
"""

import random
from individual import Individual


def create_individuals(num_of_edges, num_of_individuals=100):
    """
    Создает список особей со случайными генетическими
    кодами.

    ------Параметры------
    num_of_edges - количество ребер в графе.
    num_of_individuals - количество особей в списке.
    """
    individuals = []
    for i in range(num_of_individuals):
        indiv = Individual(random.randint(0, 2 ** num_of_edges - 1))
        individuals.append(indiv)

    return individuals


def assign_fitness(individuals, graph, fitness_func, epsilon):
    """
    Получает на вход список экземпляров класса
    Individual и считает фитнес-функцию для тех,
    у которых поле fitness является пустым.

    И строит граф для особи

    ------Параметры------
    individuals - список особей
    graph - граф
    fitness_func - фитнес-функция
    epsilon - минимальное значение фитнес-функции
    """
    for i in range(len(individuals)):
        if individuals[i].fitness != None:
            continue
        individuals[i].fitness = fitness_func(individuals[i], graph, epsilon)

def log(individuals, generation_number):
    """
    Выводит информацию о переданных особях.

    ------Параметры------
    individuals - список особей
    generation_number - номер генерации
    """
    fitness_values = [indiv.fitness for indiv in individuals]

    print("Номер генерации: ", generation_number)
    print("Лучшее значение фитнес-функции: ", max(fitness_values))

    num_of_individuals = len(individuals)
    av_fitness = sum(fitness_values) / num_of_individuals
    print("Среднее значение фитнес-функции: ", av_fitness)
    print("Количество особей в популяции: ", len(individuals))

    gen_codes = [indiv.gen_code for indiv in individuals]
    print("Количество уникальных генетических кодов:", len(list(set(gen_codes))))
    print()



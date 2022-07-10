"""
Данный файл содержит вспомогательные функции
для генетического алгоритма.
"""

import random
from genetic_algorithm.src.individual import Individual
import os.path


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

def log(individuals, generation_number, namefile=None):
    """
    Выводит информацию о переданных особях.
    Если передан путь к файлу логов (может не существовать),
    то информация записывается в него. Иначе логи выводятся
    в консоль.

    ------Параметры------
    individuals - список особей
    generation_number - номер генерации
    namefile - путь к файлу логов
    """
    log_info = ""
    fitness_values = [indiv.fitness for indiv in individuals]

    log_info += "Номер генерации: " + str(generation_number) + "\n"
    log_info += "Лучшее значение фитнес-функции: " + str(max(fitness_values)) + "\n"

    num_of_individuals = len(individuals)
    av_fitness = sum(fitness_values) / num_of_individuals
    
    log_info += "Среднее значение фитнес-функции: " + str(av_fitness) + "\n"
    log_info += "Количество особей в популяции: " + str(len(individuals)) + "\n"

    gen_codes = [indiv.gen_code for indiv in individuals]
    log_info += "Количество уникальных генетических кодов:" + str(len(list(set(gen_codes)))) + "\n"
    log_info += "\n"
    if not namefile:
        print(log_info)
    else:
        mode = 'a'
        if not os.path.exists(namefile):
            mode = 'w'
        with open(namefile, mode) as f:
            f.write(log_info)


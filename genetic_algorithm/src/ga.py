"""
Модуль реализации ген. алгоритма.

Текущее базовое решение (02.07.2022)
"""

import ga_functions as gen_algf
import graph_functions as gf
from individual import *


class GA:
    """
    Класс, реализующий инициализацию
    и запуск генетического алгоритма.
    """

    def __init__(self, convergence, num_of_individuals, selection_coefficient, \
                 probability_of_mutation, gens_mutation, \
                 num_of_generations, graph, reproduction, \
                 mutations, selection, fitness):
        """
        ------Параметры------
        convergence - кол-во уникальных особей, при достижении которого
        считается что алгоритм сошелся

        num_of_individuals - количество особей в популяции. В текущей
        версии это число фиксировано.

        selection_coefficient - количество "элитарных" особей

        probability_of_mutation - вероятность мутации особи

        gens_mutation - вероятность мутации гена
        nums_of_generations - количество генераций алгоритма

        graph - граф, минимальное остовное дерево которого надо найти

        reproduction, mutations, selection, fitness - функции кроссовера,
        мутации, отбора и фитнеса.
        """

        self.num_of_individuals = num_of_individuals
        self.selection_coefficient = selection_coefficient
        self.probability_of_mutation = probability_of_mutation
        self.gens_mutation = gens_mutation
        self.num_of_generations = num_of_generations
        self.graph = graph
        self.reproduction = reproduction
        self.mutations = mutations
        self.selection = selection
        self.fitness = fitness
        self.num_of_edges = gf.get_number_of_edges(graph)
        self.epsilon = 1 / gf.get_sum_of_edges(graph)
        self.convergence = convergence

        self.answer = None

        # установка значения аттрибута класса Individual
        Individual._len_gen_code = self.num_of_edges



    def run(self, log_cycle=100):
        individuals = gen_algf.create_individuals(self.num_of_edges, self.num_of_individuals)
        gen_algf.assign_fitness(individuals, self.graph, self.fitness, self.epsilon)

        for generation in range(0, self.num_of_generations+1):
            # логирование
            if generation % log_cycle == 0:
                gen_algf.log(individuals, generation)

            # проверка на сходимость
            gen_codes = [indiv.gen_code for indiv in individuals]
            if len(list(set(gen_codes))) <= self.convergence:
                gen_algf.log(individuals, generation)
                break

            # запуск кроссовера
            new_individuals = self.reproduction(individuals, self.num_of_edges)
            gen_algf.assign_fitness(new_individuals, self.graph, self.fitness, self.epsilon)


            # объединение потомков с родителями и произведение мутаций
            individuals += new_individuals
            mutants = self.mutations(individuals, self.probability_of_mutation, \
                                     self.gens_mutation, self.num_of_edges)

            # пересчет значений фитнес ф-и для ф-и для мутантов
            gen_algf.assign_fitness(mutants, self.graph, self.fitness, self.epsilon)

            # отбор особей в новую популяцию
            individuals = self.selection(individuals, self.num_of_individuals, \
                                         self.selection_coefficient)


    def run_by_step(self):
        result_step = {'step': 0, 'childes': [], 'mutants': [], 'new_population': []}

        # создание случайной популяции
        individuals = gen_algf.create_individuals(self.num_of_edges, self.num_of_individuals)
        gen_algf.assign_fitness(individuals, self.graph, self.fitness, self.epsilon)

        result_step['new_population'] = individuals
        yield result_step

        for generation in range(1, self.num_of_generations+1):
            result_step['step'] = generation

            # проверка на сходимость
            gen_codes = [indiv.gen_code for indiv in individuals]
            if len(list(set(gen_codes))) <= self.convergence:
                gen_algf.log(individuals, generation)
                break

            # запуск кроссовера
            new_individuals = self.reproduction(individuals, self.num_of_edges)
            gen_algf.assign_fitness(new_individuals, self.graph, self.fitness, self.epsilon)
            result_step['childes'] = new_individuals

            # объединение потомков с родителями и произведение мутаций
            individuals += new_individuals
            mutants = self.mutations(individuals, self.probability_of_mutation, \
                                     self.gens_mutation, self.num_of_edges)

            # пересчет значений фитнес ф-и для ф-и для мутантов
            gen_algf.assign_fitness(mutants, self.graph, self.fitness, self.epsilon)
            result_step['mutants'] = mutants

            # отбор особей в новую популяцию
            individuals = self.selection(individuals, self.num_of_individuals, \
                                         self.selection_coefficient)
            result_step['new_population'] = individuals

            yield result_step

        # сохранение ответа
        self.answer = max(individuals, key=lambda ind: ind.fitness)

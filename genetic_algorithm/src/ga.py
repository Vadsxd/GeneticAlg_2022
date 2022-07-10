"""
Модуль реализации ген. алгоритма.

Текущее базовое решение (02.07.2022)
"""

import genetic_algorithm.src.ga_functions as gen_algf
import genetic_algorithm.src.graph_functions as gf
import reproduction_functions as rf 
import mutations_functions as mf 
import selection_functions as sf 
import fitness_functions as ff 
from genetic_algorithm.src.individual import *
from copy import copy
from typing import Optional


class GA:
    """
    Класс, реализующий инициализацию
    и запуск генетического алгоритма.
    """

    def __init__(self, num_of_individuals=None, selection_coefficient=None, \
                 probability_of_mutation=None, gens_mutation=None, \
                 num_of_generations=None, graph=None, reproduction=rf.panmixia_reproduction, \
                 mutations=mf.gen_mutations, selection=sf.elite_selection, fitness=ff.fitness_function, convergence=0):
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

        reproduction, mutation, selection, fitness - функции кроссовера,
        мутации, отбора и фитнеса.
        """

        if graph is None:
            return

        self.num_of_individuals = num_of_individuals
        self.selection_coefficient = selection_coefficient
        self.probability_of_mutation = probability_of_mutation
        self.gens_mutation = gens_mutation
        self.num_of_generations = num_of_generations
        self.graph = graph
        self.reproduction = reproduction
        self.mutation = mutations
        self.selection = selection
        self.fitness = fitness
        self.num_of_edges = gf.get_number_of_edges(graph)
        self.epsilon = 1 / gf.get_sum_of_edges(graph)
        self.convergence = convergence

        # итоговый ответ ГА, будет None пока работает ГА
        self.answer = None  # type: Optional[Individual]

        # установка значения аттрибута класса Individual
        Individual._len_gen_code = self.num_of_edges
        Individual._initial_graph = self.graph




    def run(self, log_cycle=100):
        individuals = gen_algf.create_individuals(self.num_of_edges, self.num_of_individuals)
        gen_algf.assign_fitness(individuals, self.graph, self.fitness, self.epsilon)

        for generation in range(0, self.num_of_generations+1):
            # логирование
            if generation % log_cycle == 0:
                gen_algf.log(individuals, generation)

            # проверка на сходимость
            if self._check_convergence(individuals):
                gen_algf.log(individuals, generation)
                break

            # запуск кроссовера
            new_individuals = self.reproduction(individuals, self.num_of_edges)
            gen_algf.assign_fitness(new_individuals, self.graph, self.fitness, self.epsilon)


            # объединение потомков с родителями и произведение мутаций
            individuals += new_individuals
            self.mutation(individuals, self.probability_of_mutation, \
                                     self.gens_mutation, self.num_of_edges)


            # пересчет значений фитнес ф-и для ф-и для мутантов
            gen_algf.assign_fitness(mutants, self.graph, self.fitness, self.epsilon)

            # отбор особей в новую популяцию
            individuals = self.selection(individuals, self.num_of_individuals, \
                                         self.selection_coefficient)


    def run_by_step(self, path):
        """
        Генератор пошагово выполнения ГА. При каждом вызове создает новое поколение
        и возвращает информацию об этапах создания этого поколения.

        ------Алгоритм создания нового поколения-----
            1. Берем за основу популяцию пред. поколения.
            2. Создаем потомков (кроссинговер) на основе этой популяции и добавляем их в текущую популяцию.
            3. Производим мут-ю некоторых особей во всей популяции (мут-я может происходить как с родителями, так и с потомками)
            4. Осуществляем селекцию (отбор из образованного мн-ва особей).

        -------return-----
        Словарь, в котором есть след. ключи:
            'step' - номер поколения или шага алгоритма.
            'childes' - список потомков (класс Individual) после кроссинговера.
            'mutations' - список мутаций (класс MutationInd), каждый элемент списка содержит поле:
                 * mutant - мутировавшее состояние особи
                 * norm_indiv - норм. состояние особи.
            'new_population' - итоговая популяция данного поколения (результат этапа отбора)

        !!!!!!!Примечание!!!!!!!!
            1. Когда алгоритм сходится (или достигает заданного кол-ва поколений), вызывается исключение StopIteration.
        Итоговый ответ на задачу (лучшая особь) заносится в поле self.answer
            2. На первой итерации (step = 0) возвращаться словарь, у которого будет заполнен только список 'new_population',
        так как при старте начальная популяция создается случайно.
        """
        result_step = {'step': 0, 'childes': [], 'mutants': [], 'parents': []}

        # создание случайной популяции
        individuals = gen_algf.create_individuals(self.num_of_edges, self.num_of_individuals)
        gen_algf.assign_fitness(individuals, self.graph, self.fitness, self.epsilon)
        
        for generation in range(1, self.num_of_generations+1):
            gen_algf.log(individuals, generation, path)
            result_step['step'] = generation

            # запуск кроссовера
            new_individuals = self.reproduction(individuals, self.num_of_edges)
            gen_algf.assign_fitness(new_individuals, self.graph, self.fitness, self.epsilon) 

            # объединение потомков с родителями и произведение мутаций
            individuals += new_individuals
            self.mutation(individuals, self.probability_of_mutation, \
                                     self.gens_mutation, self.num_of_edges)


            # пересчет значений фитнес ф-и для мутантов
            gen_algf.assign_fitness(mutations, self.graph, self.fitness, self.epsilon)

            childs, mutants, parents = [], [], []
            for individual in individuals:
                if individual.status == 'parent':
                    parents.append(individual)
                elif individual.status == 'child':
                    childs.append(individual)
                elif individual.status == 'mutant':
                    mutants.append(individual)

            result_step['childes'] = childs
            result_step['mutants'] = mutants
            result_step['parents'] = parents
            yield result_step
            
            # отбор особей в новую популяцию
            individuals = self.selection(individuals, self.num_of_individuals, \
                                         self.selection_coefficient)


        # сохранение ответа
        self.answer = max(individuals, key=lambda ind: ind.fitness)

    def _check_convergence(self, individuals):
        gen_codes = [indiv.gen_code for indiv in individuals]
        return len(list(set(gen_codes))) <= self.convergence





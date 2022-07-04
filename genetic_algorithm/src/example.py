"""
Пример работы генетического алгоритма для 
полного графа на 17 вершинах. Для запуска
данного примера должен быть установлен модуль
scipy.
"""

from ga import GA
from graph_functions import create_full_graph, weight_of_min_tree
import reproduction_functions as rf
import mutations_functions as mf
import selection_functions as sf
import fitness_functions as ff


graph = create_full_graph(17)
min_weight = weight_of_min_tree(graph)  # работает на основе модуля scipy

ga = GA(convergence=0, num_of_individuals=100, selection_coefficient=0.2, probability_of_mutation=0.05, \
	gens_mutation=0.1, num_of_generations=6500, log_cycle=100, graph=graph, reproduction=rf.panmixia_reproduction,\
	mutations=mf.gen_mutations, selection=sf.elite_selection, fitness=ff.fitness_function)
ga.run()
print("Вес минимального остовного дерева:", min_weight)
print("Наилучшее значение фитнес-функции:", 1 / min_weight)





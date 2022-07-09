from genetic_algorithm.src.graph_functions import create_full_graph
from draw_graph import graph_to_png
from windows.create_graph_win.graph_func import graph_to_str
from genetic_algorithm.src.individual import Individual
from genetic_algorithm.src.ga_functions import create_individuals
import random
import sys




n = 10
graph = create_full_graph(n)
Individual._len_gen_code = (n * (n-1)) // 2
Individual._initial_graph = graph
individuals = create_individuals(Individual._len_gen_code, 10)
names_vert = [i for i in range(1, n + 1)]
#graph_to_png(graph, names_vert, out_path='graph.png')

names_vert = list(range(n))
random.shuffle(names_vert)
individual_to_png(individuals[0], graph, names_vert, out_path="indiv_graph.png")


#names = [i for i in range(n)]
#print(graph_to_str(graph, names))

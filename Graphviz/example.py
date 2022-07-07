from genetic_algorithm.src.graph_functions import create_full_graph
from draw_graph import draw_graph

n = 10
graph = create_full_graph(n)
names_vert = [i for i in range(1, n + 1)]
draw_graph(graph, names_vert, out_path='graph.png')

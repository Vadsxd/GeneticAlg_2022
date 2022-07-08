from genetic_algorithm.src.graph_functions import create_full_graph
from draw_graph import graph_to_png
from windows.create_graph_win.graph_func import graph_to_str

n = 10
graph = create_full_graph(n)
names_vert = [i for i in range(1, n + 1)]
graph_to_png(graph, names_vert, out_path='graph.png')

#names = [i for i in range(n)]
#print(graph_to_str(graph, names))

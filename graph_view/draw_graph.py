import graphviz
from typing import List
from graph_view.png_func import create_empty_png_file
import os

def graph_to_png(graph_list: List, names_vertexes, out_path: str):
    # если нечего рисовать
    if graph_list == []:
        create_empty_png_file(out_path)
        return

    view_graph = graphviz.Graph(strict=True)
    view_graph.attr('node', shape='circle')

    # создаем вершины
    for vert_ind in range(len(graph_list)):
        view_graph.node(str(names_vertexes[vert_ind]))

    # создаем ребра
    for vert1_ind, list_edges in enumerate(graph_list):
        for edges, vert2_ind in list_edges:
            view_graph.edge(str(names_vertexes[vert1_ind]), str(names_vertexes[vert2_ind]), label=str(edges))

    view_graph.render(engine='fdp', outfile=out_path)

    path_without_ext, _ = os.path.splitext(out_path)

    os.remove(path_without_ext + ".gv")




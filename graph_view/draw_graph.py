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
    view_graph.graph_attr.update(size="6,5")


    # создаем вершины
    for vert_ind in range(len(graph_list)):
        view_graph.node(str(names_vertexes[vert_ind]))

    # создаем ребра
    for vert1_ind, list_edges in enumerate(graph_list):
        for edges, vert2_ind in list_edges:
            view_graph.edge(str(names_vertexes[vert1_ind]), str(names_vertexes[vert2_ind]), label=str(edges))

    view_graph.render(engine='circo', outfile=out_path)

    path_without_ext, _ = os.path.splitext(out_path)

    os.remove(path_without_ext + ".gv")

def individual_to_png(individual, graph_list: List, names_vertexes, out_path: str):
    # если нечего рисовать
    if graph_list == []:
        create_empty_png_file(out_path)
        return

    view_graph = graphviz.Graph(strict=True)
    view_graph.attr('node', shape='circle')
    view_graph.graph_attr.update(size="6,4.2")

    # создаем вершины
    for vert_ind in range(len(graph_list)):
        view_graph.node(str(names_vertexes[vert_ind]))

    indiv_graph = individual.graph

    str_weight = ""
    # создаем ребра
    for vert1_ind, list_edges in enumerate(graph_list):
        for edges, vert2_ind in list_edges:
            edge_color = 'grey'
            str_weight = ""
            if (edges, vert2_ind) in indiv_graph[vert1_ind]:
                edge_color = 'black'
                str_weight = str(edges)

            view_graph.edge(str(names_vertexes[vert1_ind]), str(names_vertexes[vert2_ind]), label=str_weight, color=edge_color)

    view_graph.render(engine='circo', outfile=out_path)

    path_without_ext, _ = os.path.splitext(out_path)

    os.remove(path_without_ext + ".gv")












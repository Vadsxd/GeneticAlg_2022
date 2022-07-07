import graphviz
from typing import List


def graph_to_png(graph_list: List, names_vertexes, out_path: str):
    view_graph = graphviz.Graph(strict=True)
    view_graph.attr('node', shape='circle')

    # создаем вершины
    for vert_ind in range(len(graph_list)):
        view_graph.node(str(names_vertexes[vert_ind]))

    # создаем ребра
    for vert1_ind, list_edges in enumerate(graph_list):
        for edges, vert2_ind in list_edges:
            view_graph.edge(str(names_vertexes[vert1_ind]), str(names_vertexes[vert2_ind]), label=str(edges), color='gray')

    view_graph.render(engine='fdp', outfile=out_path)


def create_png_file(path: str):
    view_graph = graphviz.Graph()
    view_graph.render(outfile=path)

import windows.create_graph_win.graph_func as gr_func

def read_graph_from_file(file, ext ,graph, names_vertexes):
    """
     ext: '.txt' либо '.gv'
    """
    if ext == '.txt':
        return _read_graph_from_txt(file, graph, names_vertexes)
    if ext == '.gv':
        return _read_graph_from_gv(file, graph, names_vertexes)


def _read_graph_from_gv(file, graph, names_vertexes):
    pass


def _read_graph_from_txt(file, graph, names_vertexes):
    try:
        for line in file:
            vert1_name, vert2_name, weight = map(int, line.split())

            gr_func.add_edge(vert1_name, vert2_name, weight, graph, names_vertexes)

        return True

    except Exception:
        return False


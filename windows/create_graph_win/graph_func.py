from genetic_algorithm.src.graph_functions import depth_search


def add_edge(vert_name_1, vert_name_2, weight, graph, names_vertexes):
    # проверка на петли
    if vert_name_1 == vert_name_2:
        return False

    # проверка существования верш (добавляем их, если нет)
    if vert_name_1 not in names_vertexes:
        names_vertexes.append(vert_name_1)
        graph.append([])

    if vert_name_2 not in names_vertexes:
        names_vertexes.append(vert_name_2)
        graph.append([])

    # имя верш -> индекс верш
    ind_vert1 = names_vertexes.index(vert_name_1)
    ind_vert2 = names_vertexes.index(vert_name_2)

    # проверка на наличие ребра
    if find_edge(graph, ind_vert1, ind_vert2) is not None:
        del_edge(vert_name_1, vert_name_2, graph, names_vertexes)

    # добавляем
    graph[ind_vert1].append((weight, ind_vert2))
    graph[ind_vert2].append((weight, ind_vert1))

    return True


def del_edge(vert1_name, vert2_name, graph, names_vertexes):
    # если нет таких вершин
    if vert1_name not in names_vertexes or vert2_name not in names_vertexes:
        return False

    # имя верш -> индекс верш
    ind_vert1 = names_vertexes.index(vert1_name)
    ind_vert2 = names_vertexes.index(vert2_name)

    if (weight := find_edge(graph, ind_vert1, ind_vert2)) is None:  # значит такого ребра нет
        return False

    # удаляем ребро
    graph[ind_vert1].remove((weight, ind_vert2))
    graph[ind_vert2].remove((weight, ind_vert1))

    return True


def find_edge(graph, vert1_ind, vert2_ind):
    for some_weight, some_vert in graph[vert1_ind]:
        if some_vert == vert2_ind:
            return some_weight

    return None


def del_vert(graph, names_vertexes, vert_del_name):
    # есть ли такая вершина
    if vert_del_name not in names_vertexes:
        return False

    # имя верш -> индекс верш
    vert_del_ind = names_vertexes.index(vert_del_name)

    # удаляем вершину
    graph.pop(vert_del_ind)
    names_vertexes.pop(vert_del_ind)

    for list_edges in graph:
        len_list_edges = len(list_edges)
        i = 0
        while i < len_list_edges:
            weight, some_vert_ind = list_edges[i]

            # удаляем ребра связанные с этой вершиной
            if some_vert_ind == vert_del_ind:
                list_edges.pop(i)
                len_list_edges -= 1
                continue

            # корректируем ссылки на другие вершины
            if some_vert_ind > vert_del_ind:
                list_edges[i] = (weight, some_vert_ind - 1)

            i = i + 1


def graph_to_str(graph, names_vertexes):
    edges = set()
    string = ""

    for vert1_ind, list_edges in enumerate(graph):
        for weight, vert2_ind in list_edges:
            v_max = max(vert2_ind, vert1_ind)
            v_min = min(vert2_ind, vert1_ind)

            edges.add(f"{v_min} {v_max} {weight}")

    for edge in edges:
        string += edge
        string += '\n'

    return string


def is_connectivity_graph(graph):
    n = len(graph)  # кол-во вершин

    is_visited = [False] * n
    visited_edges = 0
    depth_search(graph, 0, is_visited, 0, visited_edges)

    if False in is_visited:
        return False
    else:
        return True

import dearpygui.dearpygui as dpg
import easygui
from graph_view.draw_graph import graph_to_png
import os
import windows.primary_win.primary_window as primary_window


graph = []
names_vertexes = []


# for button "Upload Graph"
def upload_graph():
    input_file = easygui.fileopenbox(filetypes=["*.txt"])
    file = open(input_file, 'r')
    print(*file)


# for button "Add"
def update_graph():
    vert_name_1 = dpg.get_value("Ver1")
    vert_name_2 = dpg.get_value("Ver2")
    weight = dpg.get_value("Weight")

    if not _add_edge(vert_name_1, vert_name_2, weight, graph, names_vertexes):
        return

    graph_to_png(graph, names_vertexes, out_path='.tmp_graph.png')
    _update_texture('.tmp_graph.png')


# for button "Delete Vertex"
def delete_vertex():
    vertex_name = dpg.get_value("DelVer")

    if _del_vert(graph, names_vertexes, vertex_name) == False:
        print('not')
        return

    graph_to_png(graph, names_vertexes, out_path='.tmp_graph.png')
    _update_texture('.tmp_graph.png')


# for button "Delete Edge"
def handler_button_del_edge():
    vert_name_1 = dpg.get_value("EdVer1")
    vert_name_2 = dpg.get_value("EdVer2")

    if not _del_edge(vert_name_1, vert_name_2, graph, names_vertexes):
        return

    graph_to_png(graph, names_vertexes, out_path='.tmp_graph.png')
    _update_texture('.tmp_graph.png')


def handler_button_back():
    graph.clear()
    names_vertexes.clear()
    if os.path.exists('.tmp_graph.png'):
        os.remove('.tmp_graph.png')
    if os.path.exists('.tmp_graph.gv'):
        os.remove('.tmp_graph.gv')
    primary_window.to_primary_window()


def _update_texture(path_to_png):
    width, height, channels, data = dpg.load_image(path_to_png)

    dpg.set_item_width("texture_tag", width)
    dpg.set_item_height("texture_tag", height)
    dpg.set_value("texture_tag", data)

    if dpg.does_item_exist("img"):
        dpg.delete_item("img")

    if dpg.does_item_exist("texture_tag"):
        dpg.delete_item("texture_tag")

    dpg.add_dynamic_texture(
        width=width,
        height=height,
        default_value=data,
        tag="texture_tag",
        parent="registry"
    )

    dpg.add_image(
        "texture_tag",
        tag="img",
        pos=(500, 10),
        parent="Create Window"
    )


def _add_edge(vert_name_1, vert_name_2, weight, graph, names_vertexes):
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
    if _find_edge(graph, ind_vert1, ind_vert2) is not None:
        return False

    # добавляем ребро
    graph[ind_vert1].append((weight, ind_vert2))
    graph[ind_vert2].append((weight, ind_vert1))

    return True


def _del_edge(vert1_name, vert2_name, graph, names_vertexes):
    # если нет таких вершин
    if vert1_name not in names_vertexes or vert2_name not in names_vertexes:
        return False

    # имя верш -> индекс верш
    ind_vert1 = names_vertexes.index(vert1_name)
    ind_vert2 = names_vertexes.index(vert2_name)

    if (weight := _find_edge(graph, ind_vert1, ind_vert2)) is None:  # значит такого ребра нет
        return False


    # удаляем ребро
    graph[ind_vert1].remove((weight, ind_vert2))
    graph[ind_vert2].remove((weight, ind_vert1))

    # удаляем "голые" вершины
    if graph[ind_vert1] == []:
        _del_vert(graph, names_vertexes,ind_vert1)
        if ind_vert2 > ind_vert1:
            ind_vert2 -= 1

    if graph[ind_vert2] == []:
        _del_vert(graph, names_vertexes, ind_vert2)

    return True


def _find_edge(graph, vert1_ind, vert2_ind):
    for some_weight, some_vert in graph[vert1_ind]:
        if some_vert == vert2_ind:
            return some_weight

    return None


def _del_vert(graph, names_vertexes, vert_del_name):
    print(names_vertexes)
    print(vert_del_name)
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
                list_edges[i] = (weight, some_vert_ind-1)

            i = i+1

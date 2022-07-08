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

    # проверка существования верш
    if vert_name_1 not in names_vertexes:
        names_vertexes.append(vert_name_1)
        graph.append([])

    if vert_name_2 not in names_vertexes:
        names_vertexes.append(vert_name_2)
        graph.append([])

    # имя верш -> индекс верш
    ind_vert1 = names_vertexes.index(vert_name_1)
    ind_vert2 = names_vertexes.index(vert_name_2)

    # добавляем ребра
    graph[ind_vert1].append((weight, ind_vert2))
    graph[ind_vert2].append((weight, ind_vert1))

    graph_to_png(graph, names_vertexes, out_path='.tmp_graph.png')

    width, height, channels, data = dpg.load_image('.tmp_graph.png')

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


# for button "Delete Vertex"
def delete_vertex():
    vertex = dpg.get_value("DelVer")
    print(vertex)


# for button "Delete Edge"
def delete_edge():
    vertex_1 = dpg.get_value("EdVer1")
    vertex_2 = dpg.get_value("EdVer2")
    print(vertex_1)
    print(vertex_2)


def handler_button_back():
    graph.clear()
    names_vertexes.clear()
    if os.path.exists('.tmp_graph.png'):
        os.remove('.tmp_graph.png')
    if os.path.exists('.tmp_graph.gv'):
        os.remove('.tmp_graph.gv')
    primary_window.to_primary_window()


#def handler_button_finish():
#   create_graph_window.to_create_graph()

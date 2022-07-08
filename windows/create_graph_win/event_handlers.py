import dearpygui.dearpygui as dpg
from graph_view.draw_graph import graph_to_png, create_empty_png_file
import os
import windows.primary_win.primary_window as primary_window
import os.path
from windows.create_graph_win.reader import read_graph_from_file
import windows.create_graph_win.graph_func as gr_func

from tkinter import messagebox as msg
from tkinter import filedialog as fd
from tkinter import Tk

graph = []
names_vertexes = []


def handler_button_clear():
    graph.clear()
    names_vertexes.clear()
    create_empty_png_file('.tmp_graph.png')

    graph_to_png(graph, names_vertexes, out_path='.tmp_graph.png')
    _update_texture('.tmp_graph.png')


# for button "Upload Graph"
def upload_graph():
    Tk().withdraw()  # не выводит левое окно
    path = fd.askopenfilename(title="Выберете файл",
                              filetypes=(("Graph", "*.gv;*.txt"), ("All files", "*.*"))
                              , parent=None)

    if path == '':
        return

    _, ext = os.path.splitext(path)
    if ext not in [".txt", ".gv"]:
        msg.showerror(title="Ошибка", message='Файл должен быть только с разрешением .txt или .gv')
        return

    try:
        with open(path, 'r') as file:
            if not read_graph_from_file(file, ext, graph, names_vertexes):
                msg.showerror(title="Ошибка",
                              message='Не удалось прочитать файл. Возможно некоторые данные в файле некорректные')
                return

    except OSError:
        msg.showerror(title="Ошибка", message='Не удалось открыть файл')
        return

    graph_to_png(graph, names_vertexes, out_path='.tmp_graph.png')
    _update_texture('.tmp_graph.png')


# for button "Add"
def update_graph():
    vert_name_1 = dpg.get_value("Ver1")
    vert_name_2 = dpg.get_value("Ver2")
    weight = dpg.get_value("Weight")

    if not gr_func.add_edge(vert_name_1, vert_name_2, weight, graph, names_vertexes):
        return

    graph_to_png(graph, names_vertexes, out_path='.tmp_graph.png')
    _update_texture('.tmp_graph.png')


# for button "Delete Vertex"
def delete_vertex():
    vertex_name = dpg.get_value("DelVer")

    if gr_func.del_vert(graph, names_vertexes, vertex_name) == False:
        print('not')
        return

    graph_to_png(graph, names_vertexes, out_path='.tmp_graph.png')
    _update_texture('.tmp_graph.png')


# for button "Delete Edge"
def handler_button_del_edge():
    vert_name_1 = dpg.get_value("EdVer1")
    vert_name_2 = dpg.get_value("EdVer2")

    if not gr_func.del_edge(vert_name_1, vert_name_2, graph, names_vertexes):
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

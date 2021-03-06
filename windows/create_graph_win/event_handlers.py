import dearpygui.dearpygui as dpg
from graph_view.draw_graph import graph_to_png, create_empty_png_file
import os
import windows.primary_win.primary_window as primary_window
import os.path
import windows.create_graph_win.graph_func as gr_func
import windows.alg_win.alg_window as alg_win


from tkinter import messagebox as msg
from tkinter import filedialog as fd
from tkinter import Tk

graph = []
names_vertexes = []


def block_buttons():
    dpg.disable_item("Save")
    dpg.disable_item("Back")
    dpg.disable_item("Clear")
    dpg.disable_item("Help")
    dpg.disable_item("Finish")
    dpg.disable_item("Upload Graph")
    dpg.disable_item("Add")
    dpg.disable_item("Delete Vertex")
    dpg.disable_item("Delete Edge")


def unblock_buttons():
    dpg.enable_item("Save")
    dpg.enable_item("Back")
    dpg.enable_item("Clear")
    dpg.enable_item("Help")
    dpg.enable_item("Finish")
    dpg.enable_item("Upload Graph")
    dpg.enable_item("Add")
    dpg.enable_item("Delete Vertex")
    dpg.enable_item("Delete Edge")


def handler_button_finish(sender, app_data):

    Tk().withdraw()  # не выводит левое окно

    if graph == []:
        block_buttons()
        msg.showerror(title="Ошибка", message='Введите граф')
        unblock_buttons()
        return

    if not gr_func.is_connectivity_graph(graph):
        block_buttons()
        msg.showerror(title="Ошибка", message='Граф должен быть связанный')
        unblock_buttons()
        return

    alg_win.to_alg_window(graph, names_vertexes)


def handler_button_save():
    if graph == []:
        return

    Tk().withdraw()  # не выводит левое окно
    type_files = [("All files", "*.*"),
                  ('Текст', '*.txt'),
                  ('Изображение', '*.png')]
    path = fd.asksaveasfilename(title="Сохранить как...", filetypes=type_files, defaultextension=".txt")

    if path == '':
        return

    _, ext = os.path.splitext(path)
    if ext not in [".txt", ".png"]:
        block_buttons()
        msg.showerror(title="Ошибка", message='Файл должен быть только с разрешением .txt или .png')
        unblock_buttons()
        return

    if ext == ".png":
        graph_to_png(graph, names_vertexes, out_path=path)
        return

    # если ".txt"
    try:
        with open(path, 'w') as file:
            file.write(gr_func.graph_to_str(graph, names_vertexes))

    except OSError:
        block_buttons()
        msg.showerror(title="Ошибка", message='Не удалось создать файл')
        unblock_buttons()
        return


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
                              filetypes=(("Текст", "*.txt"), ("All files", "*.*")),
                              parent=None)

    if path == '':
        return

    _, ext = os.path.splitext(path)
    if not ext == ".txt":
        block_buttons()
        msg.showerror(title="Ошибка", message='Файл должен быть только с разрешением .txt')
        unblock_buttons()
        return

    try:
        with open(path, 'r') as file:
            if not read_graph_from_file(file, graph, names_vertexes):
                block_buttons()
                msg.showerror(title="Ошибка",
                              message='Не удалось прочитать файл. Возможно некоторые данные в файле некорректные')
                unblock_buttons()
                return

    except OSError:
        block_buttons()
        msg.showerror(title="Ошибка", message='Не удалось открыть файл')
        unblock_buttons()
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
        pos=(400, 10),
        parent="Create Window"
    )


def read_graph_from_file(file, graph, names_vertexes):
    graph.clear()
    names_vertexes.clear()

    try:
        for line in file:
            if line == '\n': continue
            vert1_name, vert2_name, weight = map(int, line.split())

            gr_func.add_edge(vert1_name, vert2_name, weight, graph, names_vertexes)

        return True

    except Exception:
        return False



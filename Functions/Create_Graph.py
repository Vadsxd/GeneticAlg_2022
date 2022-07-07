import dearpygui.dearpygui as dpg
import easygui


saved_image = []


# for button "Upload Graph"
def upload_graph():
    input_file = easygui.fileopenbox(filetypes=["*.txt"])
    file = open(input_file, 'r')
    print(*file)


# for button "Add"
def update_graph():
    vertex_1 = dpg.get_value("Ver1")
    vertex_2 = dpg.get_value("Ver2")
    weight = dpg.get_value("Weight")
    print(vertex_1)
    print(vertex_2)
    print(weight)

    saved_image.clear()
    width, height, channels, data = dpg.load_image("pibs.png")
    saved_image.extend([width, height, channels, data])

    dpg.set_value("texture_tag", data)


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

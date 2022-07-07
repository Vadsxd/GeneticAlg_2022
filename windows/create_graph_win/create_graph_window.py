import dearpygui.dearpygui as dpg
from windows.alg_win.event_handlers import get_item_values
from windows.create_graph_win.event_handlers import update_graph, upload_graph, delete_vertex, delete_edge, saved_image
from windows.alg_win.alg_window import to_alg_window
import windows.primary_win.primary_window as primary_window


def to_create_graph():
    if dpg.does_item_exist("Primary Window"):
        dpg.delete_item("Primary Window")

    if dpg.does_item_exist("Window2"):
        get_item_values()
        dpg.delete_item("Window2")

    width, height, channels, data = dpg.load_image('.tmp_graph.png')

    # если изображение графа сохранялось, то загрузится оно, иначе дефолтная картинка
    if saved_image:
        with dpg.texture_registry(tag="registry"):
            dpg.add_dynamic_texture(
                width=saved_image[0],
                height=saved_image[1],
                default_value=saved_image[3],
                tag="texture_tag"
            )
    else:
        with dpg.texture_registry(tag="registry"):
            dpg.add_dynamic_texture(
                width=width,
                height=height,
                default_value=data,
                tag="texture_tag"
            )

    with dpg.window(tag="Create Window", label="Graph Menu", width=1000, height=550):
        dpg.add_button(
            label="Back",
            pos=(260, 460),
            width=100,
            height=30,
            callback=primary_window.to_primary_window
        )
        dpg.add_button(
            label="Finish",
            pos=(10, 460),
            width=120,
            height=30,
            callback=to_alg_window
        )
        dpg.add_button(
            label="Upload Graph",
            pos=(260, 420),
            width=100,
            height=30,
            callback=upload_graph
        )
        dpg.add_input_int(
            tag="Ver1",
            label="Vertex 1",
            pos=(10, 20),
            width=100,
            min_value=0,
            min_clamped=True
        )
        dpg.add_input_int(
            tag="Ver2",
            label="Vertex 2",
            pos=(10, 60),
            width=100,
            min_value=0,
            min_clamped=True
        )
        dpg.add_input_int(
            tag="Weight",
            label="Weight of Edge",
            pos=(10, 100),
            width=100,
            min_value=0,
            min_clamped=True
        )
        dpg.add_button(
            label="Add",
            pos=(260, 55),
            width=100,
            height=30,
            callback=update_graph
        )
        dpg.add_input_int(
            tag="DelVer",
            label="Vertex to Delete",
            pos=(10, 180),
            width=100,
            min_value=0,
            min_clamped=True
        )
        dpg.add_button(
            label="Delete Vertex",
            pos=(260, 175),
            width=100,
            height=30,
            callback=delete_vertex
        )
        dpg.add_input_int(
            tag="EdVer1",
            label="Vertex 1",
            pos=(10, 260),
            width=100,
            min_value=0,
            min_clamped=True
        )
        dpg.add_input_int(
            tag="EdVer2",
            label="Vertex 2",
            pos=(10, 300),
            width=100,
            min_value=0,
            min_clamped=True
        )
        dpg.add_button(
            label="Delete Edge",
            pos=(260, 280),
            width=100,
            height=30,
            callback=delete_edge
        )
        dpg.add_image(
            "texture_tag",
            tag="img",
            pos=(500, 10)
        )
        dpg.set_viewport_height(550)
        dpg.set_viewport_width(1000)
        dpg.set_primary_window("Create Window", True)


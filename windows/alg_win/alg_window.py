import dearpygui.dearpygui as dpg
from windows.alg_win.event_handlers import *
import windows.help_win.help_window as help_window
import windows.create_graph_win.create_graph_window as create_graph_win
import windows.alg_win.event_handlers as handler
from windows.alg_win.setting_func import *
from graph_view.png_func import create_empty_png_file


def to_alg_window(graph, names_vertexes):
    if dpg.does_item_exist("Help Window"):
        dpg.delete_item("Help Window")
        dpg.show_item("Window2")

    if dpg.does_item_exist("Create Window"):
        dpg.delete_item("registry")
        dpg.delete_item("Create Window")
        if dpg.does_item_exist("Window2"):
            dpg.show_item("Window2")

    ga_alg = ga.GA()
    dict_name_indiv = {}


    # создаем новый файл png
    width_img = 255
    height_img =255
    data = create_empty_png_file('.indiv.png', width_img, height_img)


    if not dpg.does_item_exist("Window2"):
        # создание дин. структуры
        with dpg.texture_registry(tag="registry2"):
            dpg.add_dynamic_texture(
                width=width_img,
                height=height_img,
                default_value=data,
                tag="texture_tag2"
            )
        with dpg.window(tag="Window2", label="Graph Menu", width=1000, height=550):
            dpg.add_listbox(items=[], label="Population", tag="listbox", callback=handler_click_listbox, width=270,
                            num_items=9, user_data=(graph, names_vertexes, dict_name_indiv))
            dpg.add_button(
                label="Back",
                pos=(260, 460),
                width=100,
                height=30,
                callback=handler_button_back
            )
            dpg.add_button(
                label="Next",
                tag="button_next_alg",
                pos=(10, 460),
                width=120,
                height=30,
                enabled=False,
                show=False,
                callback=handler_button_next,
            )
            dpg.add_button(
                label="Start Algorithm",
                tag="button_start_alg",
                pos=(10, 460),
                width=120,
                height=30,
                callback=handler_button_start_alg,
                user_data=(ga_alg, graph, names_vertexes, dict_name_indiv)
            )
            dpg.add_button(
                label="Stop Algorithm",
                pos=(10, 420),
                width=120,
                height=30,
                callback=handler_button_stop
            )
            dpg.add_button(
                label="Help",
                pos=(145, 470),
                width=100,
                height=20,
                callback=help_window.to_help_window
            )
            dpg.add_button(
                label="Reset",
                pos=(260, 430),
                width=100,
                height=20,
                callback=handler_button_reset
            )
            dpg.add_slider_float(
                tag="Gens Mutation Slider",
                label="Gens Mutation",
                pos=(10, 190),
                default_value=0.1,
                max_value=1,
                width=180,
                height=30
            )
            dpg.add_slider_int(
                tag="Number of Generations Slider",
                label="Number of Generations",
                pos=(10, 230),
                default_value=1000,
                max_value=3000,
                width=180,
                height=30
            )
            dpg.add_slider_int(
                tag="Number of Individuals Slider",
                label="Number of Individuals",
                pos=(10, 270),
                default_value=100,
                max_value=1000,
                width=180,
                height=30
            )
            dpg.add_slider_float(
                tag="Selection Coefficient Slider",
                label="Selection Coefficient",
                pos=(10, 310),
                default_value=0.1,
                max_value=1,
                width=180,
                height=30
            )
            dpg.add_slider_float(
                tag="Probability of Mutation Slider",
                label="Probability of Mutation",
                pos=(10, 350),
                default_value=0.05,
                max_value=1,
                width=180,
                height=30
            )
            dpg.add_image(
                "texture_tag2",
                tag="indiv_img",
                pos=(390, 60)
            )

    dpg.set_viewport_height(550)
    dpg.set_viewport_width(1000)
    dpg.set_primary_window("Window2", True)

    if settings:
        set_item_values()

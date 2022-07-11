import genetic_algorithm.src.ga as ga
import genetic_algorithm.src.graph_functions as gf
from windows.alg_win.setting_func import *
import windows.create_graph_win.create_graph_window as create_graph_win
from graph_view.draw_graph import individual_to_png

import os
from typing import List, Tuple, Dict

ga_alg = None

# for button "Iterable/To End"
def change_mode():
    if dpg.get_item_label("Mode of Visualisation") == "To End":
        dpg.set_item_label("Mode of Visualisation", "Iterable")
    else:
        dpg.set_item_label("Mode of Visualisation", "To End")


# for button "Button/SlideShow"
def change_transition_mode():
    if dpg.get_item_label("Transition Mode") == "Button":
        dpg.set_item_label("Transition Mode", "SlideShow")
    else:
        dpg.set_item_label("Transition Mode", "Button")


def handler_button_stop():
    if dpg.is_item_enabled("button_next_alg"):
        # замена next button
        dpg.disable_item("button_next_alg")
        dpg.hide_item("button_next_alg")

        dpg.show_item("button_start_alg")
        dpg.enable_item("button_start_alg")

        # разблокировка ползунков
        dpg.enable_item("Gens Mutation Slider")
        dpg.enable_item("Number of Generations Slider")
        dpg.enable_item("Number of Individuals Slider")
        dpg.enable_item("Selection Coefficient Slider")
        dpg.enable_item("Probability of Mutation Slider")

        dpg.enable_item("button_reset")


# for button "Start Algorithm"
def handler_button_start_alg(sender, app_data, param: List):
    graph, names_vert, dict_name_indiv = param

    get_item_values()  # заполнили settings

    # замена start button
    dpg.disable_item("button_start_alg")
    dpg.hide_item("button_start_alg")

    dpg.show_item("button_next_alg")
    dpg.enable_item("button_next_alg")

    # блокировка ползунков
    dpg.disable_item("Gens Mutation Slider")
    dpg.disable_item("Number of Generations Slider")
    dpg.disable_item("Number of Individuals Slider")
    dpg.disable_item("Selection Coefficient Slider")
    dpg.disable_item("Probability of Mutation Slider")
    dpg.disable_item("button_reset")

    # удаляем старый лог
    if os.path.exists(".log.txt"):
        os.remove(".log.txt")

    global ga_alg
    ga_alg = ga.GA(*settings, graph)

    # хрень полная
    ga_alg.generator = ga_alg.run_by_step(".log.txt")

    handler_button_next(sender, app_data, (graph, names_vert, dict_name_indiv))




def handler_button_next(sender, app_data, param):
    graph, names_vert, dict_name_indiv = param

    global ga_alg

    ga_step = next(ga_alg.generator)

    dpg.set_item_label("listbox", "Generation: " + str(ga_step["step"]))

    # именуем особи
    i = 1
    for indiv in ga_step["parents"]:
        name = "Parents " + str(i)
        dict_name_indiv[name] = indiv
        i += 1

    i = 1
    for indiv in ga_step["childes"]:
        name = "Child " + str(i)
        dict_name_indiv[name] = indiv
        i += 1

    print(ga_step)

    i = 1
    for indiv in ga_step["mutants"]:
        name = "Mutant " + str(i)
        dict_name_indiv[name] = indiv
        i += 1

    # сортируем имена
    tmp = sorted(dict_name_indiv.items(), key=lambda x: x[1].fitness, reverse=True)
    data_listbox = [x[0] for x in tmp]

    # обновляем listbox
    dpg.configure_item("listbox", items=data_listbox)

    # отобразить первую особь в списке
    handler_click_listbox("listbox", data_listbox[0], (graph, names_vert, dict_name_indiv))


def handler_button_reset():
    settings.clear()
    dpg.set_value("Number of Generations Slider", 1000)
    settings.append(1000)

    dpg.set_value("Number of Individuals Slider", 100)
    settings.append(100)

    dpg.set_value("Gens Mutation Slider", 0.1)
    settings.append(0.1)

    dpg.set_value("Selection Coefficient Slider", 0.1)
    settings.append(0.1)

    dpg.set_value("Probability of Mutation Slider", 0.05)
    settings.append(0.05)


def handler_button_back():
    # замена next button
    if dpg.is_item_enabled("button_next_alg"):
        dpg.disable_item("button_next_alg")
        dpg.hide_item("button_next_alg")

        dpg.show_item("button_start_alg")
        dpg.enable_item("button_start_alg")

    dpg.configure_item("listbox", items=[])
    get_item_values()
    create_graph_win.to_create_graph()


def handler_click_listbox(sender, app_data, param):
    graph, names_vertexes, dict_name_indiv = param
    indiv = dict_name_indiv[app_data]

    message = "Individual: --" + app_data + "--\nGenetic code: " + indiv.str_gen_code() + "\n"

    weight_of_tree = gf.get_sum_of_edges(indiv.graph)
    message += "Weight of individual graph: " + str(weight_of_tree) + "\n"
    message += "Fitness value: " + str(indiv.fitness) + "\n"

    dpg.set_value("inf_indiv", message)
    individual_to_png(indiv, graph, names_vertexes, ".indiv.png")
    _update_texture(".indiv.png")


def _update_texture(path_to_png):
    width, height, channels, data = dpg.load_image(path_to_png)

    dpg.set_item_width("texture_tag2", width)
    dpg.set_item_height("texture_tag2", height)
    dpg.set_value("texture_tag2", data)

    if dpg.does_item_exist("indiv_img"):
        dpg.delete_item("indiv_img")

    if dpg.does_item_exist("texture_tag2"):
        dpg.delete_item("texture_tag2")

    dpg.add_dynamic_texture(
        width=width,
        height=height,
        default_value=data,
        tag="texture_tag2",
        parent="registry2"
    )

    dpg.add_image(
        "texture_tag2",
        tag="indiv_img",
        pos=(390, 80),
        parent="Window2"
    )

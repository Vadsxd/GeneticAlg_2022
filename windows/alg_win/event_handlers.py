import genetic_algorithm.src.ga as ga
from windows.alg_win.setting_func import *
import windows.create_graph_win.create_graph_window as create_graph_win
from graph_view.draw_graph import individual_to_png
import genetic_algorithm.src.graph_functions as gf
from graph_view.png_func import create_empty_png_file
from genetic_algorithm.src.graph_functions import weight_of_min_tree

import os
from typing import List, Tuple, Dict

ga_alg = None


def handler_button_end(sender, app_data, param):
    # listbox
    dpg.configure_item("listbox", items=[])

    # image clear
    width_img = 255
    height_img = 255
    create_empty_png_file('.indiv.png', width_img, height_img)
    _update_texture('.indiv.png')

    # блок. кноп
    dpg.disable_item("Back")
    dpg.disable_item("button_next_alg")
    dpg.disable_item("To End")
    dpg.disable_item("To End")
    dpg.disable_item("Stop Algorithm")
    dpg.disable_item("Help")
    dpg.disable_item("button_reset")

    i = 0
    while handler_button_next(sender, app_data, (*param, 0)):
        # text info
        if i % 400 == 0:
            dpg.set_value("inf_indiv", "Loading")

        if i % 400 == 100:
            dpg.set_value("inf_indiv", "Loading.")

        if i % 400 == 200:
            dpg.set_value("inf_indiv", "Loading..")

        if i % 400 == 300:
            dpg.set_value("inf_indiv", "Loading...")

        i += 1
        pass


    # блок. кноп
    dpg.enable_item("Back")
    dpg.enable_item("button_next_alg")
    dpg.enable_item("To End")
    dpg.enable_item("To End")
    dpg.enable_item("Stop Algorithm")
    dpg.enable_item("Help")
    dpg.enable_item("button_reset")
    dpg.disable_item("To End")


def handler_button_stop():
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
    dpg.disable_item("To End")

    dpg.set_value("inf_indiv", "")
    dpg.set_item_label("listbox", "Population")
    dpg.configure_item("listbox", items=[])
    width_img = 255
    height_img = 255
    create_empty_png_file('.indiv.png', width_img, height_img)
    _update_texture('.indiv.png')


# for button "Start Algorithm"
def handler_button_start_alg(sender, app_data, param: List):
    graph, names_vert, dict_name_indiv = param

    print(weight_of_min_tree(graph))

    get_item_values()  # заполнили settings

    dpg.configure_item("inf_indiv", color=[255, 255, 255])

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

    dpg.enable_item("To End")

    # удаляем старый лог
    if os.path.exists(".log.txt"):
        os.remove(".log.txt")

    global ga_alg
    ga_alg = ga.GA(*settings, graph)

    # хрень полная
    ga_alg.generator = ga_alg.run_by_step(".log.txt")

    handler_button_next(sender, app_data, (graph, names_vert, dict_name_indiv, 1))


def handler_button_next(sender, app_data, param):
    graph, names_vert, dict_name_indiv, vis = param

    generation = None
    try:
        generation = _processing_step_ga(dict_name_indiv)
    except Exception:
        _processing_end_step(graph, names_vert)
        return False

    # сортируем имена
    tmp = sorted(dict_name_indiv.items(), key=lambda x: x[1].fitness, reverse=True)
    data_listbox = [x[0] for x in tmp]

    dpg.set_item_label("listbox", f"Generation:{generation}")

    if vis:
        # обновляем listbox
        dpg.configure_item("listbox", items=data_listbox)

        # отобразить первую особь в списке
        handler_click_listbox("listbox", data_listbox[0], (graph, names_vert, dict_name_indiv))
        dpg.configure_item("listbox", default_value=data_listbox[0])

    return True


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


def _processing_step_ga(dict_name_indiv):
    """
     Заполняет словарь dict_name_indiv по ключам - имена особей,
        а по значению - сами особи текущего поколения

    :return:
        поколение (числом)
    """

    global ga_alg

    ga_step = next(ga_alg.generator)

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

    i = 1
    for indiv in ga_step["mutants"]:
        name = "Mutant " + str(i)
        dict_name_indiv[name] = indiv
        i += 1

    return ga_step["step"]


def _processing_end_step(graph, names_vertexes):
    dpg.set_item_label("listbox", "End")

    # обновляем listbox
    dpg.configure_item("listbox", items=[])

    global ga_alg
    indiv = ga_alg.answer

    dpg.configure_item("inf_indiv", color=[0, 255, 0])

    message = "Best Individual\nGenetic code: " + indiv.str_gen_code() + "\n"

    weight_of_tree = gf.get_sum_of_edges(indiv.graph)
    message += "Weight of individual graph: " + str(weight_of_tree) + "\n"
    message += "Fitness value: " + str(indiv.fitness) + "\n"

    dpg.set_value("inf_indiv", message)

    individual_to_png(indiv, graph, names_vertexes, ".indiv.png")
    _update_texture(".indiv.png")

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
    dpg.disable_item("To End")

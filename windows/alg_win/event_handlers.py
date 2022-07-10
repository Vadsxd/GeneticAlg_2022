import dearpygui.dearpygui as dpg
from windows.alg_win.SeriesData import SeriesData
import genetic_algorithm.src.ga as ga
from windows.alg_win.setting_func import *
import  windows.create_graph_win.create_graph_window as create_graph_win

import genetic_algorithm.src.reproduction_functions as rf
import genetic_algorithm.src.mutations_functions as mf
import genetic_algorithm.src.selection_functions as sf
import genetic_algorithm.src.fitness_functions as ff

import os
from typing import List, Tuple


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


# for button "Start Algorithm"
def handler_button_start_alg(sender, app_data, param: Tuple[ga.GA, List]):
    ga_alg, graph = param

    get_item_values()  # заполнили settings

    # замена start button
    dpg.disable_item("button_start_alg")
    dpg.hide_item("button_start_alg")

    dpg.show_item("button_next_alg")
    dpg.enable_item("button_next_alg")

    ga_alg = ga.GA(convergence=0, num_of_individuals=10, selection_coefficient=0.2, probability_of_mutation=0.05, \
            gens_mutation=0.1, num_of_generations=1000, graph=graph, reproduction=rf.panmixia_reproduction, \
            mutations=mf.gen_mutations, selection=sf.elite_selection, fitness=ff.fitness_function)

    # удаляем старый лог
    if os.path.exists(".log.txt"):
        os.remove(".log.txt")

    step_ga = {}
    step_ga = next(ga_alg.run_by_step(".log.txt"))

    # заполняем данные





def handler_button_next():
    pass

def handler_button_back():
    # замена next button
    if dpg.is_item_enabled("button_next_alg"):
        dpg.disable_item("button_next_alg")
        dpg.hide_item("button_next_alg")

        dpg.show_item("button_start_alg")
        dpg.enable_item("button_start_alg")

    create_graph_win.to_create_graph()



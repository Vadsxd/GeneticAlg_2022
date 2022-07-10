import dearpygui.dearpygui as dpg
from windows.alg_win.event_handlers import *
import windows.help_win.help_window as help_window
import windows.create_graph_win.create_graph_window as create_graph_win
import windows.alg_win.event_handlers as handler
from windows.alg_win.setting_func import *



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

    if not dpg.does_item_exist("Window2"):
        with dpg.window(tag="Window2", label="Graph Menu", width=1000, height=550):
            dpg.add_text(
                "Menu for graph customization",
                pos=(50, 20)
            )
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
                callback = handler_button_next
            )
            dpg.add_button(
                label="Start Algorithm",
                tag="button_start_alg",
                pos=(10, 460),
                width=120,
                height=30,
                callback=handler_button_start_alg,
                user_data=(ga_alg, graph)
            )
            dpg.add_button(
                label="Stop Algorithm",
                pos=(10, 420),
                width=120,
                height=30
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
                callback=reset_settings
            )
            dpg.add_slider_float(
                tag="Gens Mutation Slider",
                label="Gens Mutation",
                pos=(10, 160),
                default_value=0.1,
                max_value=1,
                width=180,
                height=30
            )
            dpg.add_slider_int(
                tag="Number of Generations Slider",
                label="Number of Generations",
                pos=(10, 200),
                default_value=1000,
                max_value=3000,
                width=180,
                height=30
            )
            dpg.add_slider_int(
                tag="Number of Individuals Slider",
                label="Number of Individuals",
                pos=(10, 240),
                default_value=100,
                max_value=1000,
                width=180,
                height=30
            )
            dpg.add_slider_float(
                tag="Selection Coefficient Slider",
                label="Selection Coefficient",
                pos=(10, 280),
                default_value=0.1,
                max_value=1,
                width=180,
                height=30
            )
            dpg.add_slider_float(
                tag="Probability of Mutation Slider",
                label="Probability of Mutation",
                pos=(10, 320),
                default_value=0.05,
                max_value=1,
                width=180,
                height=30
            )
            dpg.add_slider_int(
                tag="Log Cycle Slider",
                label="Log Cycle",
                pos=(10, 360),
                default_value=50,
                max_value=100,
                width=180,
                height=30
            )
            dpg.add_text(
                "Mode of Visualisation",
                pos=(140, 55)
            )
            dpg.add_button(
                tag="Mode of Visualisation",
                label="Iterable",
                pos=(10, 50),
                width=120,
                height=30,
                callback=change_mode
            )
            dpg.add_text(
                "Transition Mode",
                pos=(140, 95)
            )
            dpg.add_button(
                tag="Transition Mode",
                label="Button",
                pos=(10, 90),
                width=120,
                height=30,
                callback=change_transition_mode
            )



    dpg.set_viewport_height(550)
    dpg.set_viewport_width(1000)
    dpg.set_primary_window("Window2", True)

    if settings:
        set_item_values()

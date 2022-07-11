import dearpygui.dearpygui as dpg

from windows.alg_win.event_handlers import get_item_values
import windows.alg_win.alg_window as alg_win
from windows.help_win.event_handlers import *


def to_help_window():
    if dpg.does_item_exist("Window2"):
        dpg.hide_item("Window2")

    with dpg.window(tag="Help Window", label="Help Menu", width=620, height=500):
        dpg.add_text(
            "Information page!",
            pos=(200, 20)
        )
        dpg.add_text(
            "Gens Mutation - probability of gen's mutation",
            pos=(70, 50)
        )
        dpg.add_text(
            "Number of Generations - number of steps (generations) in algorithm",
            pos=(70, 80)
        )
        dpg.add_text(
            "Number of Individuals - amount of individuals in current population",
            pos=(70, 110)
        )
        dpg.add_text(
            "Selection Coefficient - amount of 'elite' individuals",
            pos=(70, 140)
        )
        dpg.add_text(
            "Probability of Mutation - probability of individual's mutation",
            pos=(70, 170)
        )
        dpg.add_text(
            "How to start algorithm: choose parameters in slides then click 'Start Algorithm'",
            pos=(30, 200)
        )
        dpg.add_text(
            "button. Then to the next step click button 'Next', to the end of alg 'To End'.",
            pos=(30, 215)
        )
        dpg.add_text(
            "To check individuals scroll window in the left bottom and click one individual.",
            pos=(30, 230)
        )
        dpg.add_text(
            "You can stop algorithm on any step just press Stop Algorithm, but graph will be",
            pos=(30, 245)
        )
        dpg.add_text(
            "removed so you can construct params in a different way.",
            pos=(30, 260)
        )
        dpg.add_text(
            "When algorithm work you can't interact with slides and reset them. For this stop",
            pos=(30, 275),
            color=(255, 0, 0)
        )
        dpg.add_text(
            "alg pressing 'Stop Algorithm.'",
            pos=(30, 290),
            color=(255, 0, 0)
        )
        dpg.add_button(
            label="Back",
            pos=(490, 410),
            width=100,
            height=30,
            callback=handler_button_back
        )
    dpg.set_viewport_height(500)
    dpg.set_viewport_width(620)
    dpg.set_primary_window("Help Window", True)

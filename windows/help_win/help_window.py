import dearpygui.dearpygui as dpg

from windows.alg_win.event_handlers import get_item_values



def to_help_window():
    if dpg.does_item_exist("Window2"):
        get_item_values()
        dpg.delete_item("Window2")

    with dpg.window(tag="Help Window", label="Help Menu", width=620, height=500):
        dpg.add_text(
            "This page can help you :)",
            pos=(150, 20)
        )
        dpg.add_button(
            label="Back",
            pos=(490, 410),
            width=100,
            height=30,
            callback=to_alg_window
        )
    dpg.set_viewport_height(500)
    dpg.set_viewport_width(620)
    dpg.set_primary_window("Help Window", True)

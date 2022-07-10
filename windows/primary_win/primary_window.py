import dearpygui.dearpygui as dpg
from windows.alg_win.setting_func import settings
from windows.primary_win.event_handlers import end_prog
import windows.create_graph_win.create_graph_window as create_graph_win


def to_primary_window():
    if dpg.does_item_exist("Window2"):  # alg_win
        settings.clear()
        dpg.delete_item("Window2")

    if dpg.does_item_exist("Help Window"):
        dpg.delete_item("Help Window")

    if dpg.does_item_exist("Create Window"):
        dpg.delete_item("Create Window")
        dpg.delete_item("registry")

    with dpg.window(tag="Primary Window", label="Greeting Window", width=620, height=350):
        dpg.add_text(
            "Greetings Dear User!",
            pos=(170, 20)
        )
        dpg.add_text(
            "This program was made to find minimal spanning tree",
            pos=(110, 50)
        )
        dpg.add_text(
            "If you want to upload graph by the file just press Upload Graph",
            pos=(80, 80)
        )
        dpg.add_text(
            "If you want construct graph press Create Graph",
            pos=(100, 110)
        )
        dpg.add_text(
            "For more information press Help (after you load graph)",
            pos=(100, 140)
        )
        dpg.add_button(
            label="Exit Program",
            pos=(480, 260),
            width=100,
            height=30,
            callback=end_prog
        )
        dpg.add_button(
            label="Create Graph",
            pos=(20, 260),
            width=100,
            height=30,
            callback=create_graph_win.to_create_graph
        )
    dpg.set_viewport_height(350)
    dpg.set_viewport_width(620)
    dpg.set_primary_window("Primary Window", True)


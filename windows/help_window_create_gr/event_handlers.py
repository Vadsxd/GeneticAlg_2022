import dearpygui.dearpygui as dpg


def handler_button_back():
    if dpg.does_item_exist("Create Window"):
        dpg.delete_item("Help Window Create Gr")
        dpg.show_item("Create Window")
        dpg.set_viewport_height(550)
        dpg.set_viewport_width(1000)
        dpg.set_primary_window("Create Window", True)

import dearpygui.dearpygui as dpg


def handler_button_back():
    if dpg.does_item_exist("Window2"):
        dpg.delete_item("Help Window")
        dpg.show_item("Window2")
        dpg.set_viewport_height(550)
        dpg.set_viewport_width(1000)
        dpg.set_primary_window("Window2", True)

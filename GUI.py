import dearpygui.dearpygui as dpg
import windows.primary_win.primary_window as primary_window
from windows.handler_exit_program import handler_exit_program

dpg.create_context()
dpg.create_viewport(title='Genetic Program', width=620, height=350, resizable=False)
dpg.set_viewport_large_icon("icon.ico")
dpg.set_viewport_small_icon("icon.ico")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_exit_callback(handler_exit_program)

primary_window.to_primary_window()

dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()


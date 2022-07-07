import dearpygui.dearpygui as dpg
import windows.primary_win.primary_window as primary_window

dpg.create_context()

dpg.create_viewport(title='Genetic Program', width=620, height=350)
dpg.setup_dearpygui()
dpg.show_viewport()

primary_window.to_primary_window()

dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()

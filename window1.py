import dearpygui.dearpygui as dpg
import window2


def end_prog():
    exit(0)


def start_alg():
    window2.alg_menu()


dpg.create_context()

with dpg.window(tag="Primary Window", label="Greeting Window", width=620, height=350):
    dpg.add_text("Graphical Interface for Program :)", pos=(150, 20))
    dpg.add_button(label="Exit Program", pos=(490, 260), width=100, height=30, callback=end_prog)
    dpg.add_button(label="Upload Graph", pos=(120, 260), width=100, height=30)
    dpg.add_button(label="Create Graph", pos=(10, 260), width=100, height=30, callback=start_alg)

dpg.create_viewport(title='Greeting Window', width=620, height=350)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()

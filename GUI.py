import dearpygui.dearpygui as dpg


def end_prog():
    exit(0)


def to_primary_window():
    if dpg.does_item_exist("Window2"):
        dpg.delete_item("Window2")
    with dpg.window(tag="Primary Window", label="Greeting Window", width=620, height=350):
        dpg.add_text("Graphical Interface for Program :)", pos=(150, 20))
        dpg.add_button(label="Exit Program", pos=(490, 260), width=100, height=30, callback=end_prog)
        dpg.add_button(label="Upload Graph", pos=(120, 260), width=100, height=30)
        dpg.add_button(label="Create Graph", pos=(10, 260), width=100, height=30, callback=to_alg_window)
    dpg.set_viewport_height(350)
    dpg.set_viewport_width(620)
    dpg.set_primary_window("Primary Window", True)


def to_alg_window():
    dpg.delete_item("Primary Window")
    sindatax = []
    sindatay = []
    for i in range(0, 20):
        sindatax.append(i)
        sindatay.append(i * 2)
    sindatay = sindatay[::-1]

    with dpg.window(tag="Window2", label="Graph Menu", width=1000, height=550):
        dpg.add_text("Menu for graph customization", pos=(50, 20))
        dpg.add_button(label="Back", pos=(200, 460), width=100, height=30, callback=to_primary_window)
        dpg.add_button(label="Start Algorithm", pos=(10, 460), width=120, height=30)
        dpg.add_button(label="Stop Algorithm", pos=(10, 420), width=120, height=30)
        dpg.add_slider_int(label="Size of Population", pos=(10, 200), default_value=0, max_value=100, width=200,
                           height=30)
        # Иттерационное отображение алгоритма или сразу в конец
        dpg.add_button(label="I/E", pos=(80, 50), width=120, height=30)
        # Слайдшоу или переход от иттерации по кнопке
        dpg.add_button(label="B/S", pos=(80, 90), width=120, height=30)

        with dpg.plot(label="Algorithm Graphic", height=470, width=600, pos=(350, 20)):
            # dpg.add_plot_legend()
            dpg.add_plot_axis(dpg.mvXAxis, label="Generation")
            dpg.add_plot_axis(dpg.mvYAxis, label="Tree Weight", tag="y_axis")
            for i in range(0, 20):
                dpg.add_drag_point(color=[255, 0, 0], default_value=(sindatax[i], sindatay[i]), callback=end_prog)
            # dpg.add_line_series(sindatax, sindatay, parent="y_axis")
        dpg.set_viewport_height(550)
        dpg.set_viewport_width(1000)
        dpg.set_primary_window("Window2", True)
    # window2.alg_menu()


dpg.create_context()

dpg.create_viewport(title='Genetic Program', width=620, height=350)
dpg.setup_dearpygui()
dpg.show_viewport()

to_primary_window()

dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()

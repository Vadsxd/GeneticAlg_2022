import dearpygui.dearpygui as dpg


sindatax = []
sindatay = []
for i in range(0, 20):
    sindatax.append(i)
    sindatay.append(i*2)
sindatay = sindatay[::-1]


def exit_m():
    exit(0)


def alg_menu():
    dpg.create_context()

    with dpg.window(tag="Primary Window", label="Graph Menu", width=1000, height=550):
        dpg.add_text("Menu for graph customization", pos=(50, 20))
        dpg.add_button(label="Back", pos=(200, 460), width=100, height=30)
        dpg.add_slider_int(label="Size of Population", pos=(10, 200), default_value=0, max_value=100, width=200, height=30)
        dpg.add_button(label="Start Algorithm", pos=(10, 460), width=120, height=30)
        # Иттерационное отображение алгоритма или сразу в конец
        dpg.add_button(label="I/E", pos=(80, 50), width=120, height=30)
        # Слайдшоу или переход от иттерации по кнопке
        dpg.add_button(label="B/S", pos=(80, 90), width=120, height=30)

        with dpg.plot(label="Algorithm Graphic", height=250, width=400, pos=(500, 20)):
            # dpg.add_plot_legend()
            dpg.add_plot_axis(dpg.mvXAxis, label="Generation")
            dpg.add_plot_axis(dpg.mvYAxis, label="Tree Weight", tag="y_axis")
            for _ in range(0, 20):
                dpg.add_drag_point(color=[255, 0, 0], default_value=(sindatax[i], sindatay[i]), callback=exit_m)
            dpg.add_line_series(sindatax, sindatay, parent="y_axis")

    dpg.create_viewport(title="Graph Menu", width=1000, height=550)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("Primary Window", True)
    dpg.start_dearpygui()
    dpg.destroy_context()


# alg_menu()
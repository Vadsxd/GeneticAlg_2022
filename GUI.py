import dearpygui.dearpygui as dpg


def end_prog():
    exit(0)


def graphic_usage():
    print(1)


def to_primary_window():
    if dpg.does_item_exist("Window2"):
        dpg.delete_item("Window2")
    if dpg.does_item_exist("Help Window"):
        dpg.delete_item("Help Window")
    with dpg.window(tag="Primary Window", label="Greeting Window", width=620, height=350):
        dpg.add_text("Greetings Dear User!", pos=(170, 20))
        dpg.add_text("This program was made to find minimal spanning tree", pos=(110, 50))
        dpg.add_text("If you want to upload graph by the file just press Upload Graph", pos=(80, 80))
        dpg.add_text("If you want construct graph press Create Graph", pos=(100, 110))
        dpg.add_text("For more information press Help (after you load graph)", pos=(100, 140))
        dpg.add_button(label="Exit Program", pos=(490, 260), width=100, height=30, callback=end_prog)
        dpg.add_button(label="Upload Graph", pos=(120, 260), width=100, height=30)
        dpg.add_button(label="Create Graph", pos=(10, 260), width=100, height=30, callback=to_alg_window)
    dpg.set_viewport_height(350)
    dpg.set_viewport_width(620)
    dpg.set_primary_window("Primary Window", True)


def to_help_window():
    if dpg.does_item_exist("Window2"):
        dpg.delete_item("Window2")
    with dpg.window(tag="Help Window", label="Help Menu", width=620, height=500):
        dpg.add_text("This page can help you :)", pos=(150, 20))
        dpg.add_button(label="Back", pos=(490, 410), width=100, height=30, callback=to_alg_window)
    dpg.set_viewport_height(500)
    dpg.set_viewport_width(620)
    dpg.set_primary_window("Help Window", True)


def to_alg_window():
    if dpg.does_item_exist("Help Window"):
        dpg.delete_item("Help Window")
    if dpg.does_item_exist("Primary Window"):
        dpg.delete_item("Primary Window")
    sindatax = []
    sindatay = []
    for i in range(0, 20):
        sindatax.append(i)
        sindatay.append(i * 2)
    sindatay = sindatay[::-1]

    with dpg.window(tag="Window2", label="Graph Menu", width=1000, height=550):
        dpg.add_text("Menu for graph customization", pos=(50, 20))
        dpg.add_button(label="Back", pos=(260, 460), width=100, height=30, callback=to_primary_window)
        dpg.add_button(label="Start Algorithm", pos=(10, 460), width=120, height=30)
        dpg.add_button(label="Stop Algorithm", pos=(10, 420), width=120, height=30)
        dpg.add_button(label="Help", pos=(145, 470), width=100, height=20, callback=to_help_window)
        dpg.add_slider_int(label="Number of Generations", pos=(10, 200), default_value=1000, max_value=3000, width=180,
                           height=30)
        dpg.add_slider_int(label="Number of Individuals", pos=(10, 240), default_value=100, max_value=1000, width=180,
                           height=30)
        dpg.add_slider_float(label="Selection Coefficient", pos=(10, 280), default_value=0.1, max_value=1, width=180,
                             height=30)
        dpg.add_slider_float(label="Probability of Mutation", pos=(10, 320), default_value=0.05, max_value=1, width=180,
                             height=30)
        dpg.add_slider_int(label="Log Cycle", pos=(10, 360), default_value=50, max_value=100, width=180,
                           height=30)
        # Иттерационное отображение алгоритма или сразу в конец
        dpg.add_button(label="I/E", pos=(80, 50), width=120, height=30)
        # Слайдшоу или переход от иттерации по кнопке
        dpg.add_button(label="B/S", pos=(80, 90), width=120, height=30)

        with dpg.plot(label="Algorithm Graphic", height=470, width=600, pos=(370, 20)):
            dpg.add_plot_axis(dpg.mvXAxis, label="Generation")
            dpg.add_plot_axis(dpg.mvYAxis, label="Tree Weight", tag="y_axis")
            for i in range(0, 20):
                dpg.add_drag_point(color=[255, 0, 0], default_value=(sindatax[i], sindatay[i]), thickness=0.7,
                                   callback=graphic_usage)
            dpg.add_line_series(sindatax, sindatay, parent="y_axis")
        dpg.set_viewport_height(550)
        dpg.set_viewport_width(1000)
        dpg.set_primary_window("Window2", True)


dpg.create_context()

dpg.create_viewport(title='Genetic Program', width=620, height=350)
dpg.setup_dearpygui()
dpg.show_viewport()

to_primary_window()

dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()

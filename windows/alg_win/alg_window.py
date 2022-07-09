import dearpygui.dearpygui as dpg
from windows.alg_win.event_handlers import change_mode, change_transition_mode, start_algorithm, \
    reset_settings, settings, set_item_values

import windows.help_win.help_window as help_window
import windows.create_graph_win.create_graph_window as create_graph_win

sindatax = []
sindatay = []
for i in range(0, 20):
    sindatax.append(i)
    sindatay.append(i * 2)
sindatay = sindatay[::-1]

sindatax2 = []
sindatay2 = []
for i in range(0, 20):
    sindatax2.append(i)
    sindatay2.append(i * 2 + 3)
sindatay2 = sindatay2[::-1]

sindatax3 = []
sindatay3 = []
for i in range(0, 20):
    sindatax3.append(i)
    sindatay3.append(i * 2 - 5)
sindatay3 = sindatay3[::-1]


def func(sender, app_data):
    _helper_data = app_data[0]
    transformed_x = app_data[1]
    transformed_y = app_data[2]
    mouse_x_pixel_space = _helper_data["MouseX_PixelSpace"]
    mouse_y_pixel_space = _helper_data["MouseY_PixelSpace"]
    if dpg.does_item_exist(sender):
        dpg.delete_item(sender, children_only=True, slot=2)
        dpg.push_container_stack(sender)
    dpg.configure_item("demo_custom_series", tooltip=False)
    for i in range(0, len(transformed_x)):
        dpg.draw_circle((transformed_x[i], transformed_y[i]), 4, fill=(255, 0, 0))
        if transformed_x[i] + 4 > mouse_x_pixel_space > transformed_x[i] - 4 and \
                transformed_y[i] - 4 < mouse_y_pixel_space < transformed_y[i] + 4:
            dpg.draw_circle((transformed_x[i], transformed_y[i]), 7)
            dpg.configure_item("demo_custom_series", tooltip=True)
            dpg.set_value("custom_series_text", "Graph Weight: " + str(sindatay[i]) + "\n" + "Generation: " + str(i))

            if dpg.is_key_pressed(13):
                print(i)
                print(sindatay[i])
                print(dpg.get_item_label("demo_custom_series"))

    dpg.pop_container_stack()


def func2(sender, app_data):
    _helper_data = app_data[0]
    transformed_x = app_data[1]
    transformed_y = app_data[2]
    mouse_x_pixel_space = _helper_data["MouseX_PixelSpace"]
    mouse_y_pixel_space = _helper_data["MouseY_PixelSpace"]
    if dpg.does_item_exist(sender):
        dpg.delete_item(sender, children_only=True, slot=2)
        dpg.push_container_stack(sender)
    dpg.configure_item("demo_custom_series2", tooltip=False)
    for i in range(0, len(transformed_x)):
        dpg.draw_circle((transformed_x[i], transformed_y[i]), 4, fill=(0, 255, 0))
        if transformed_x[i] + 4 > mouse_x_pixel_space > transformed_x[i] - 4 and \
                transformed_y[i] - 4 < mouse_y_pixel_space < transformed_y[i] + 4:
            dpg.draw_circle((transformed_x[i], transformed_y[i]), 6)
            dpg.configure_item("demo_custom_series2", tooltip=True)
            dpg.set_value("custom_series_text2", "Graph Weight: " + str(sindatay2[i]) + "\n" + "Generation: " + str(i))

            if dpg.is_key_pressed(13):
                print(i)
                print(sindatay2[i])
                print(dpg.get_item_label("demo_custom_series2"))

    dpg.pop_container_stack()


def func3(sender, app_data):
    _helper_data = app_data[0]
    transformed_x = app_data[1]
    transformed_y = app_data[2]
    mouse_x_pixel_space = _helper_data["MouseX_PixelSpace"]
    mouse_y_pixel_space = _helper_data["MouseY_PixelSpace"]
    if dpg.does_item_exist(sender):
        dpg.delete_item(sender, children_only=True, slot=2)
        dpg.push_container_stack(sender)
    dpg.configure_item("demo_custom_series3", tooltip=False)
    for i in range(0, len(transformed_x)):
        dpg.draw_circle((transformed_x[i], transformed_y[i]), 4, fill=(0, 0, 255))
        if transformed_x[i] + 4 > mouse_x_pixel_space > transformed_x[i] - 4 and \
                transformed_y[i] - 4 < mouse_y_pixel_space < transformed_y[i] + 4:
            dpg.draw_circle((transformed_x[i], transformed_y[i]), 6)
            dpg.configure_item("demo_custom_series3", tooltip=True)
            dpg.set_value("custom_series_text3", "Graph Weight: " + str(sindatay3[i]) + "\n" + "Generation: " + str(i))

            if dpg.is_key_pressed(13):
                print(i)
                print(sindatay3[i])
                print(dpg.get_item_label("demo_custom_series3"))

    dpg.pop_container_stack()


def to_alg_window(graph, names_vertexes):
    if dpg.does_item_exist("Help Window"):
        dpg.delete_item("Help Window")
        dpg.show_item("Window2")

    if dpg.does_item_exist("Create Window"):
        dpg.delete_item("registry")
        dpg.delete_item("Create Window")
        if dpg.does_item_exist("Window2"):
            dpg.show_item("Window2")

    if not dpg.does_item_exist("Window2"):
        with dpg.window(tag="Window2", label="Graph Menu", width=1000, height=550):
            dpg.add_text(
                "Menu for graph customization",
                pos=(50, 20)
            )
            dpg.add_button(
                label="Back",
                pos=(260, 460),
                width=100,
                height=30,
                callback=create_graph_win.to_create_graph
            )
            dpg.add_button(
                label="Start Algorithm",
                pos=(10, 460),
                width=120,
                height=30,
                callback=start_algorithm
            )
            dpg.add_button(
                label="Stop Algorithm",
                pos=(10, 420),
                width=120,
                height=30
            )
            dpg.add_button(
                label="Help",
                pos=(145, 470),
                width=100,
                height=20,
                callback=help_window.to_help_window
            )
            dpg.add_button(
                label="Reset",
                pos=(260, 430),
                width=100,
                height=20,
                callback=reset_settings
            )
            dpg.add_slider_float(
                tag="Gens Mutation Slider",
                label="Gens Mutation",
                pos=(10, 160),
                default_value=0.1,
                max_value=1,
                width=180,
                height=30
            )
            dpg.add_slider_int(
                tag="Number of Generations Slider",
                label="Number of Generations",
                pos=(10, 200),
                default_value=1000,
                max_value=3000,
                width=180,
                height=30
            )
            dpg.add_slider_int(
                tag="Number of Individuals Slider",
                label="Number of Individuals",
                pos=(10, 240),
                default_value=100,
                max_value=1000,
                width=180,
                height=30
            )
            dpg.add_slider_float(
                tag="Selection Coefficient Slider",
                label="Selection Coefficient",
                pos=(10, 280),
                default_value=0.1,
                max_value=1,
                width=180,
                height=30
            )
            dpg.add_slider_float(
                tag="Probability of Mutation Slider",
                label="Probability of Mutation",
                pos=(10, 320),
                default_value=0.05,
                max_value=1,
                width=180,
                height=30
            )
            dpg.add_slider_int(
                tag="Log Cycle Slider",
                label="Log Cycle",
                pos=(10, 360),
                default_value=50,
                max_value=100,
                width=180,
                height=30
            )
            dpg.add_text(
                "Mode of Visualisation",
                pos=(140, 55)
            )
            dpg.add_button(
                tag="Mode of Visualisation",
                label="Iterable",
                pos=(10, 50),
                width=120,
                height=30,
                callback=change_mode
            )
            dpg.add_text(
                "Transition Mode",
                pos=(140, 95)
            )
            dpg.add_button(
                tag="Transition Mode",
                label="Button",
                pos=(10, 90),
                width=120,
                height=30,
                callback=change_transition_mode
            )

            with dpg.plot(label="Algorithm Graphic", height=470, width=600, pos=(370, 20), tag="Plot"):
                dpg.add_plot_legend()
                dpg.add_plot_axis(dpg.mvXAxis)
                with dpg.plot_axis(dpg.mvYAxis):

                    with dpg.custom_series(sindatax, sindatay, 2, label="Parents", callback=func,
                                           tag="demo_custom_series"):
                        dpg.add_text("Current Point: ", tag="custom_series_text")

                    with dpg.custom_series(sindatax2, sindatay2, 2, label="Mutants", callback=func2,
                                           tag="demo_custom_series2"):
                        dpg.add_text("Current Point: ", tag="custom_series_text2")

                    with dpg.custom_series(sindatax3, sindatay3, 2, label="Descendants", callback=func3,
                                           tag="demo_custom_series3"):
                        dpg.add_text("Current Point: ", tag="custom_series_text3")

                    dpg.fit_axis_data(dpg.top_container_stack())

    dpg.set_viewport_height(550)
    dpg.set_viewport_width(1000)
    dpg.set_primary_window("Window2", True)

    if settings:
        set_item_values()

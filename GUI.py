import dearpygui.dearpygui as dpg
from Functions.Primary_Window import end_prog
from Functions.Algorithm_Window import change_mode, change_transition_mode, graphic_usage, start_algorithm, \
    reset_settings, get_item_values, settings, set_item_values
from Functions.Create_Graph import update_graph, upload_graph, delete_vertex, delete_edge, saved_image


def to_primary_window():
    if dpg.does_item_exist("Window2"):
        settings.clear()
        dpg.delete_item("Window2")

    if dpg.does_item_exist("Help Window"):
        dpg.delete_item("Help Window")

    if dpg.does_item_exist("Create Window"):
        saved_image.clear()
        dpg.delete_item("registry")
        dpg.delete_item("Create Window")

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
            callback=to_create_graph
        )
    dpg.set_viewport_height(350)
    dpg.set_viewport_width(620)
    dpg.set_primary_window("Primary Window", True)


def to_help_window():
    if dpg.does_item_exist("Window2"):
        get_item_values()
        dpg.delete_item("Window2")

    with dpg.window(tag="Help Window", label="Help Menu", width=620, height=500):
        dpg.add_text(
            "This page can help you :)",
            pos=(150, 20)
        )
        dpg.add_button(
            label="Back",
            pos=(490, 410),
            width=100,
            height=30,
            callback=to_alg_window
        )
    dpg.set_viewport_height(500)
    dpg.set_viewport_width(620)
    dpg.set_primary_window("Help Window", True)


def to_alg_window():
    if dpg.does_item_exist("Help Window"):
        dpg.delete_item("Help Window")

    if dpg.does_item_exist("Create Window"):
        dpg.delete_item("registry")
        dpg.delete_item("Create Window")

    sindatax = []
    sindatay = []
    for i in range(0, 20):
        sindatax.append(i)
        sindatay.append(i * 2)
    sindatay = sindatay[::-1]

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
            callback=to_create_graph
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
            callback=to_help_window
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

        with dpg.plot(label="Algorithm Graphic", height=470, width=600, pos=(370, 20)):
            dpg.add_plot_axis(
                dpg.mvXAxis,
                label="Generation"
            )
            dpg.add_plot_axis(
                dpg.mvYAxis,
                label="Tree Weight",
                tag="y_axis"
            )
            for i in range(0, 20):
                dpg.add_drag_point(
                    color=[255, 0, 0],
                    default_value=(sindatax[i], sindatay[i]),
                    thickness=0.7,
                    callback=graphic_usage
                )
            dpg.add_line_series(
                sindatax,
                sindatay,
                parent="y_axis"
            )
        dpg.set_viewport_height(550)
        dpg.set_viewport_width(1000)
        dpg.set_primary_window("Window2", True)

    if settings:
        set_item_values()


def to_create_graph():
    if dpg.does_item_exist("Primary Window"):
        dpg.delete_item("Primary Window")

    if dpg.does_item_exist("Window2"):
        get_item_values()
        dpg.delete_item("Window2")

    width, height, channels, data = dpg.load_image(".tmp_graph.png")

    # если изображение графа сохранялось, то загрузится оно, иначе дефолтная картинка
    if saved_image:
        with dpg.texture_registry(tag="registry"):
            dpg.add_dynamic_texture(
                width=saved_image[0],
                height=saved_image[1],
                default_value=saved_image[3],
                tag="texture_tag"
            )
    else:
        with dpg.texture_registry(tag="registry"):
            dpg.add_dynamic_texture(
                width=width,
                height=height,
                default_value=data,
                tag="texture_tag"
            )

    with dpg.window(tag="Create Window", label="Graph Menu", width=1000, height=550):
        dpg.add_button(
            label="Back",
            pos=(260, 460),
            width=100,
            height=30,
            callback=to_primary_window
        )
        dpg.add_button(
            label="Finish",
            pos=(10, 460),
            width=120,
            height=30,
            callback=to_alg_window
        )
        dpg.add_button(
            label="Upload Graph",
            pos=(260, 420),
            width=100,
            height=30,
            callback=upload_graph
        )
        dpg.add_input_int(
            tag="Ver1",
            label="Vertex 1",
            pos=(10, 20),
            width=100,
            min_value=0,
            min_clamped=True
        )
        dpg.add_input_int(
            tag="Ver2",
            label="Vertex 2",
            pos=(10, 60),
            width=100,
            min_value=0,
            min_clamped=True
        )
        dpg.add_input_int(
            tag="Weight",
            label="Weight of Edge",
            pos=(10, 100),
            width=100,
            min_value=0,
            min_clamped=True
        )
        dpg.add_button(
            label="Add",
            pos=(260, 55),
            width=100,
            height=30,
            callback=update_graph
        )
        dpg.add_input_int(
            tag="DelVer",
            label="Vertex to Delete",
            pos=(10, 180),
            width=100,
            min_value=0,
            min_clamped=True
        )
        dpg.add_button(
            label="Delete Vertex",
            pos=(260, 175),
            width=100,
            height=30,
            callback=delete_vertex
        )
        dpg.add_input_int(
            tag="EdVer1",
            label="Vertex 1",
            pos=(10, 260),
            width=100,
            min_value=0,
            min_clamped=True
        )
        dpg.add_input_int(
            tag="EdVer2",
            label="Vertex 2",
            pos=(10, 300),
            width=100,
            min_value=0,
            min_clamped=True
        )
        dpg.add_button(
            label="Delete Edge",
            pos=(260, 280),
            width=100,
            height=30,
            callback=delete_edge
        )
        dpg.add_image(
            "texture_tag",
            tag="img",
            pos=(500, 10)
        )
        dpg.set_viewport_height(550)
        dpg.set_viewport_width(1000)
        dpg.set_primary_window("Create Window", True)


dpg.create_context()

dpg.create_viewport(title='Genetic Program', width=620, height=350)
dpg.setup_dearpygui()
dpg.show_viewport()

to_primary_window()

dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()

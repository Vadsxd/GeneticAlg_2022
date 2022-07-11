from windows.help_window_create_gr.event_handlers import *


def to_help_window():
    if dpg.does_item_exist("Create Window"):
        dpg.hide_item("Create Window")

    with dpg.window(tag="Help Window Create Gr", label="Help Menu", width=620, height=500):
        dpg.add_text(
            "Information page for constructing graph!",
            pos=(140, 20)
        )
        dpg.add_text(
            "If you want to add vertex just write node names, weight and press 'Add'",
            pos=(60, 50)
        )
        dpg.add_text(
            "If you want to delete vertex just write node names and press 'Delete Vertex'",
            pos=(60, 80)
        )
        dpg.add_text(
            "If you want to delete edge just write nodes names and press 'Delete Edge'",
            pos=(60, 110)
        )
        dpg.add_text(
            "To clear graph press 'Clear'",
            pos=(60, 140)
        )
        dpg.add_text(
            "To save graph press 'Save' on .txt file or a picture",
            pos=(60, 170)
        )
        dpg.add_text(
            "If you want to rollback on primary window press back (graph doesn't save)",
            pos=(60, 200)
        )
        dpg.add_text(
            "If you want to upload graph from your folder press 'Upload Graph'",
            pos=(60, 230)
        )
        dpg.add_text(
            "If you done with graph just press 'Finish' and you go to Alg window",
            pos=(60, 260)
        )
        dpg.add_text(
            "How does it work: you adding vertexes and graph prints on a right side of the",
            pos=(30, 290)
        )
        dpg.add_text(
            "window. Then you edit it and finish your creation.",
            pos=(30, 320)
        )
        dpg.add_text(
            "Warnings: disconnected graph, zero edges, no graph, incorrect .txt when upload",
            pos=(30, 350),
            color=(255, 0, 0)
        )
        dpg.add_button(
            label="Back",
            pos=(490, 410),
            width=100,
            height=30,
            callback=handler_button_back
        )
    dpg.set_viewport_height(500)
    dpg.set_viewport_width(620)
    dpg.set_primary_window("Help Window Create Gr", True)

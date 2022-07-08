import dearpygui.dearpygui as dpg


def create_empty_png_file(path: str, width=255, height=255):
    data = []
    for i in range(width * height):
        data.append(0)  # R
        data.append(0)  # G
        data.append(0)  # B
        data.append(0)  # A

    dpg.save_image(file=path, width=width, height=height, data=data, components=4)

    return data

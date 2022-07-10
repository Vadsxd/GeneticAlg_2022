import dearpygui.dearpygui as dpg

settings = []

# for button "Reset"
def reset_settings():
    settings.clear()
    dpg.set_value("Number of Generations Slider", 1000)
    settings.append(1000)
    dpg.set_value("Number of Individuals Slider", 100)
    settings.append(100)
    dpg.set_value("Gens Mutation Slider", 0.1)
    settings.append(0.1)
    dpg.set_value("Selection Coefficient Slider", 0.1)
    settings.append(0.1)
    dpg.set_value("Probability of Mutation Slider", 0.05)
    settings.append(0.05)
    dpg.set_value("Log Cycle Slider", 50)
    settings.append(50)
    dpg.set_item_label("Mode of Visualisation", "Iterable")
    settings.append("Iterable")
    dpg.set_item_label("Transition Mode", "Button")
    settings.append("Button")


# gets all values from sliders
def get_item_values():
    settings.clear()
    num_of_generations = dpg.get_value("Number of Generations Slider")
    settings.append(num_of_generations)
    num_of_individuals = dpg.get_value("Number of Individuals Slider")
    settings.append(num_of_individuals)
    gens_mutation = round(dpg.get_value("Gens Mutation Slider"), 3)
    settings.append(gens_mutation)
    selection_coefficient = round(dpg.get_value("Selection Coefficient Slider"), 3)
    settings.append(selection_coefficient)
    probability_of_mutation = round(dpg.get_value("Probability of Mutation Slider"), 3)
    settings.append(probability_of_mutation)
    log_cycle = dpg.get_value("Log Cycle Slider")
    settings.append(log_cycle)
    mode = dpg.get_item_label("Mode of Visualisation")
    settings.append(mode)
    transition_mode = dpg.get_item_label("Transition Mode")
    settings.append(transition_mode)




# sets values to sliders
def set_item_values():
    dpg.set_value("Number of Generations Slider", settings[0])
    dpg.set_value("Number of Individuals Slider", settings[1])
    dpg.set_value("Gens Mutation Slider", settings[2])
    dpg.set_value("Selection Coefficient Slider", settings[3])
    dpg.set_value("Probability of Mutation Slider", settings[4])
    dpg.set_value("Log Cycle Slider", settings[5])
    dpg.set_item_label("Mode of Visualisation", settings[6])
    dpg.set_item_label("Transition Mode", settings[7])


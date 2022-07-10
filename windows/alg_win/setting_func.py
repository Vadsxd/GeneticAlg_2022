import dearpygui.dearpygui as dpg

settings = []


# gets all values from sliders
def get_item_values():
    settings.clear()
    num_of_individuals = dpg.get_value("Number of Individuals Slider")
    settings.append(num_of_individuals)

    selection_coefficient = round(dpg.get_value("Selection Coefficient Slider"), 3)
    settings.append(selection_coefficient)

    probability_of_mutation = round(dpg.get_value("Probability of Mutation Slider"), 3)
    settings.append(probability_of_mutation)

    gens_mutation = round(dpg.get_value("Gens Mutation Slider"), 3)
    settings.append(gens_mutation)

    num_of_generations = dpg.get_value("Number of Generations Slider")
    settings.append(num_of_generations)


# sets values to sliders
def set_item_values():
    dpg.set_value("Number of Individuals Slider", settings[0])
    dpg.set_value("Selection Coefficient Slider", settings[1])
    dpg.set_value("Probability of Mutation Slider", settings[2])
    dpg.set_value("Gens Mutation Slider", settings[3])
    dpg.set_value("Number of Generations Slider", settings[4])



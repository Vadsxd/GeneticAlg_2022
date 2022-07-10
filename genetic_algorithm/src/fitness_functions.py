"""
Данный файл содержит различные фитнес-функции.

------Соглашение о реализуемых фитнес-функциях------
Фитнес-функция не должна быть меньше либо равна 0. Это
условие создано для комфортного использования функции
random.choices в функциях отбора.

"""

from genetic_algorithm.src.graph_functions import individual_to_graph, tree_cost, get_number_of_edges


def fitness_function(individual, init_graph, epsilon):
    """
    Фитнес функция, вычисляющая значение по
    следующему принципу:
    -- если гентический код особи представляет не дерево,
    то возвращается малое значение (epsilon)
    -- в противном случае возвращается величина
    1 / вес дерева

    ------Параметры------
    individual - особь
    init_graph - граф
    epsilon - малое положительное значение
    """

    answer = 1 / tree_cost(individual.graph, init_graph)
    if answer == 0:
        answer += epsilon
    n = len(init_graph)
    num_edges = get_number_of_edges(individual.graph)
    answer -= 2 * epsilon * abs(num_edges - n + 1) / (abs(n ** 2 - 3 * n + 2))
    return answer




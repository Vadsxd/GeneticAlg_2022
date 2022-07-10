from genetic_algorithm.src.graph_functions import individual_to_graph, tree_cost

class Individual:
    """
    Класс, представляющий одну особь.
    """
    _len_gen_code = None  # длины ген. кода (одинак. для всех особ. в одном ГА)
    _initial_graph = None  # исходный граф (одинак. для всех особ. в одном ГА)

    def __init__(self, code, fit=None, status='parent'):
        # граф особи
        self.graph = individual_to_graph(code, self._initial_graph)
        self.status = status # статус: родитель, потомок или мутант
        self.gen_code = code  # генетический код (в бин-ном формате)
        self.fitness = fit  # значение фитнес-функции



    def str_gen_code(self):
        return format(self.gen_code, f"0^{Individual._len_gen_code}b")

    def __repr__(self):
        return self.str_gen_code()




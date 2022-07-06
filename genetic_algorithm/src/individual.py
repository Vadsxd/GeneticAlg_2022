class Individual:
    """
    Класс, представляющий одну особь.
    """
    _len_gen_code = None

    def __init__(self, code, fit=None):
        self.graph = None
        self.gen_code = code  # генетический код (в бин-ном формате)
        self.fitness = fit  # значение фитнес-функции
        self.weight_graph = None

    def str_gen_code(self):
        return format(self.gen_code, f"0^{Individual._len_gen_code}b")

    def __repr__(self):
        return self.str_gen_code()


#class Descendant(Individual):





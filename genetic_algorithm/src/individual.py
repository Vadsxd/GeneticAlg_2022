
class Individual:
    """
    Класс, представляющий одну особь.
    """
    def __init__(self, code, fit=None):
        self.graph = None
        self.gen_code = code # генетический код
        self.fitness = fit # значение фитнес-функции

"""
Файл, содержащий функции мутации.

------Соглашение о реализуемых функциях мутации------
Реализуемая функция не должна ничего возвращать. Гены особей
меняются в передаваемом списке. Поле fitness особи с измененным
генетическим кодом должно быть установлено в None. Это необходимо
для пересчета значений фитнес-функций для мутировавших особей.
"""

import random

def gen_mutations(individuals, probability_of_mutation, gens_mutation, num_of_gens):
    """
    Функция, осуществляющая двоичную мутацию над некоторыми из
    переданных особей с заданной вероятностью. Каждый
    ген особи мутирует с вероятностью мутации гена.

    ------Параметры------
    individuals - список особей
    probability_of_mutation - вероятность мутации особи
    gens_mutation - вероятность мутации гена
    nums_of_gens - длина генетического кода особей
    """
    ch = random.choices([False, True], [1 - probability_of_mutation, probability_of_mutation], k=len(individuals))
    for i in range(len(individuals)):
        if ch[i]:
            mutate(individuals[i], gens_mutation, num_of_gens)
            individuals[i].fitness = None

def mutate(individual, prob, num_of_gens):
    """
    Осуществляет двоичную мутацию генов особи с
    заданной вероятностью.

    ------Параметры------
    individual - экземпляр класса Individual
    prob - вероятность мутации гена
    num_of_gens - длина генетического кода
    """
    mask = 1
    for i in range(num_of_gens):
        event = random.uniform(0., 1.)
        if event <= prob:
            # прибавить к гену 1 по модулю 2
            individual.gen_code = individual.gen_code ^ mask
        mask = mask << 1


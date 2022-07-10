"""
Файл, содержащий функции мутации.

------Соглашение о реализуемых функциях мутации------
Реализуемая функция должна вернуть список мутаций MutationInd, особей которые подверглись мутации.
В процессе выполнения переданное мн-во особой меняется (в результате мн-во уже будет включать мут-ов)
Поле fitness особи с измененным генетическим кодом должно быть установлено в None. Это необходимо
для пересчета значений фитнес-функций для мутировавших особей.
"""

import random
from dataclasses import dataclass
from genetic_algorithm.src.individual import Individual



@dataclass
class MutationInd:
    """
    Класс мутации одной особи.

    ----Поля----
        mutant - мутировавшее состояние особи.
        norm_indiv - нормальное (без мутации) состояние особи.
    """
    mutant: Individual
    norm_indiv: Individual


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

    ------Результат------
    Список мутаций MutationInd, каждой мут. особи
    """

    # выбираем особей для мутации
    ch = random.choices([False, True], [1 - probability_of_mutation, probability_of_mutation], k=len(individuals))
    list_mutation = []

    for i in range(len(individuals)):
        if ch[i]:
            # производим мутацию особи
            mut_indiv = mutate(individuals[i], gens_mutation, num_of_gens)

            # заменяем особь в популяции на мут.
            individuals[i] = mut_indiv.mutant

            # сохраняем мутацию
            list_mutation.append(mut_indiv)

    return list_mutation


def mutate(individual, prob, num_of_gens):
    """
    Осуществляет двоичную мутацию генов особи с
    заданной вероятностью.

    ------Параметры------
    individual - экземпляр класса Individual
    prob - вероятность мутации гена
    num_of_gens - длина генетического кода

    ------Результат------
    Объект класса MutationInd, хранящий модифицированную
    особь и нормальную
    """

    new_gen_code = individual.gen_code

    # мутируем ген. код особи
    mask = 1
    for i in range(num_of_gens):
        event = random.uniform(0., 1.)
        if event <= prob:
            # прибавить к гену 1 по модулю 2
            new_gen_code = new_gen_code ^ mask
        mask = mask << 1

    # создаем новую особь по мут. коду
    mutant = Individual(new_gen_code)

    # создаем объект MutationInd
    mut_indiv = MutationInd(norm_indiv=individual, mutant=mutant)

    return mut_indiv


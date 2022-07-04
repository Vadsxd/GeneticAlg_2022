"""
Файл, содержащий функции отбора.

------Соглашение о реализуемых функциях отбора------
Функция возвращает список отобранных особей
(экземпляры класса Individual)
"""

import random


def elite_selection(individuals, num_of_individuals, coefficient):
    """
    Функция, производящая элитарный отбор, т. е.
    в новую популяцию попадает доля лучших особей,
    остальные особи отбираются случайным образом с
    равной вероятностью. Возвращает список особей,
    прошедших отбор.

    ------Параметры------
    individuals - список особей
    num_of_individuals - количество особей, которое необходимо
    отобрать в следующую популяцию
    coefficient - доля лучших особей в новой популяции
    """

    num_elite = int(coefficient * num_of_individuals)
    num_others = num_of_individuals - num_elite

    # сортировка особей по убыванию значения фитнес-функции
    individuals.sort(key=lambda x: x.fitness, reverse=True)
    elite, others = individuals[:num_elite], individuals[num_elite:]

    # выбор случайных особей
    new_individuals = random.choices(individuals, k=num_others)
    return elite + new_individuals



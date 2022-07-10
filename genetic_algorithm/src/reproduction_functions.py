"""
Данный файл содержит функции кроссовера.

------Соглашение о реализуемых функциях кроссовера------
Функция кроссовера должна выдавать на выход список созданных особей.
"""

from genetic_algorithm.src.individual import Individual
import random

def uniform_reproduction(individuals, num_of_gens):
    """
    Функция, генерирующая новых особей с помощью
    однородного кроссовера с выбором родителей по принципу рулетки.
    Возвращает список новых особей, длина которого равна длине переданного
    списка особей, который будет использоваться для выбора
    родителей.

    ------Параметры------
    individuals - список родителей
    num_of_gens - длина генетического кода (количество ребер в графе)
    """

    num_of_indiv = len(individuals)

    new_individuals = [] # список новых особей

    # вероятность выбора особи в качестве родителя прямо
    # пропорциональна значению фитнес-функции
    weights = [individual.fitness for individual in individuals]

    ones = int(2 ** num_of_gens - 1) # единичная маска

    # два родителя генерируют двух потомков
    for i in range(num_of_indiv):
        x, y = random.choices(individuals, weights, k=2)
        mask = random.randint(1, 2 ** (num_of_gens - 1))
        first, second = (x.gen_code & mask) + ((mask ^ ones) & y.gen_code), \
                        (y.gen_code & mask) + ((mask ^ ones) & x.gen_code)
        new_individuals.append(Individual(first))
        new_individuals.append(Individual(second))
    return new_individuals

def panmixia_reproduction(individuals, num_of_gens):
    """
    Функция, генерерующая новых особей с помощью 
    однородного кроссовера с выбором родителей методом
    панмиксии. Каждая пара родителей воспроизводит
    одного потомка.

    ------Параметры------
    individuals - список родителей
    num_of_gens - длина генетического кода (количество ребер в графе)
    """
    
    num_of_indiv = len(individuals)
    new_individuals = []
    ones = int(2 ** num_of_gens - 1) # единичная маска

    # случайный выбор второго родителя
    y = [random.randint(0, num_of_indiv-1) for i in range(num_of_indiv)]
    
    for x in range(num_of_indiv):
        mask = random.randint(1, 2 ** (num_of_gens - 1))
        child = (individuals[x].gen_code & mask) + (individuals[y[x]].gen_code & (mask ^ ones))
        new_child = Individual(child)
        new_child.status = "child"
        new_individuals.append(new_child)
    return new_individuals
# Задача 13
# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = [1.1, 1.2, 3.1, 5, 10.01]


def delta_maxfloat_minfloat(list):
    my_list_max = max(my_list)
    my_list_max_int = int(my_list_max)
    drobnya_chast_max = my_list_max-my_list_max_int
    my_list_min = min(my_list)
    my_list_min_int = int(my_list_min)
    drobnya_chast_min = my_list_min-my_list_min_int
    print(my_list)
    print('max значение =', my_list_max)
    print('min значение =', my_list_min)
    print('Разница дробной части между max и min равна',
          round(drobnya_chast_max-drobnya_chast_min, 3))


delta_maxfloat_minfloat(my_list)

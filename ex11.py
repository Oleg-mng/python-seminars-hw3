# Задача 11
# Задайте список из нескольких чисел. Напишите программу, которая
# найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

my_list = [26, 12, 3, 17, 87, 29, 11, 13, 23, 3]


def sum_of_elements(list):
    sum_list = 0
    for i in range(len(my_list)):
        if (i % 2) != 0:
            sum_list += my_list[i]
    i += 2
    print('сумма элементов на нечетных позициях равна S=', sum_list)


sum_of_elements(my_list)

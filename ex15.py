# Задача 15
# Задайте число. Составьте список чисел Фибоначчи, в том числе
# для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibonachi_all():
    f = int(input('введите десятичное число:'))
    my_list = [0, 1]
    for i in range(2, f+1):
        my_list.append(my_list[i-1]+my_list[i-2])
        # print(my_list)
        list_fibonachi_minus = []
    for j in range(1, len(my_list)):
        list_fibonachi_minus.append(-my_list[-j])
        # print(list_fibonachi_minus)
        list_fibonacchi_all = list_fibonachi_minus+my_list
    print(list_fibonacchi_all)

fibonachi_all()

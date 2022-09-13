# Задача 12
# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list_base = [2, 3, 4, 5, 6, 7, 8, 9]
def compl(list1):
    list_find = []
    for i in range(int((len(list_base))/2)+1):
        comp = list_base[i]*list_base[-1-i]
        list_find.append(comp)
    if len(list_base) % 2 == 0:
        # list_find.delete([-1])
        list_find.pop()
    print(list_find)
compl(list_base)

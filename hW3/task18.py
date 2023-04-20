'''Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному
числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X'''

import  random
count_list = int(input("Введите количество элементов в списке: "))
min_value = int(input("Введите минимальное значение для заполнения списка: "))
max_value = int(input("Введите максимальное значение для заполнения списка: "))
list = [random.randint(min_value, max_value) for i in range(count_list)]
print(list)
x_value = int(input("Введите искомое число: "))
index_el = 0
min_value_el = abs(x_value - list[0])
for i in range(1, count_list):
    temp_el = abs(x_value - list[i])
    if temp_el < min_value_el:
        min_value_el = temp_el
        index_el = i
print(f"Самый близкий по величине элемент к заданному числу {list[index_el]}")
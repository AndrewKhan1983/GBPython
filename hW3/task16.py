'''Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X'''

import  random
count_list = int(input("Введите количество элементов в списке: "))
min_value = int(input("Введите минимальное значение для заполнения списка: "))
max_value = int(input("Введите максимальное значение для заполнения списка: "))
list = [random.randint(min_value, max_value) for i in range(count_list)]
print(list)
x_value = int(input("Введите искомое число: "))
count = 0
for i in list:
    if i == x_value:
        count += 1
print(count)
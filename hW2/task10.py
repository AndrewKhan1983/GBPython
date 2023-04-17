# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а
# некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть
# Вариант решения без цикла
'''import random
a = int(input("Введите количество монет: "))
orel = random.randint(1,a)
reshka = a-orel
print(f"Орлов: {orel}")
print(f"Решек: {reshka}")
if orel>reshka or orel == reshka:
    print(f"Минимальное количество монет которое нужно перевернуть равно: {reshka}")
else:
    print(f"Минимальное количество монет которое нужно перевернуть равно: {orel}")'''
# Вариант решения с циклом
n = int(input("Введите количество монет"))
count_orel = 0
count_reshka = 0
for i in range(n):
    x = int(input())
    if x == 0:
        count_orel += 1
    else:
        count_reshka += 1
if count_reshka > count_orel:
    print(count_orel)
else:
    print(count_reshka)
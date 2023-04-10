# Задача 2: Найдите сумму цифр трехзначного числа.
#
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |
from unittest import result

a = input ("Введите трехзначное число")
a1 = int(a[0])
a2 = int(a[1])
a3 = int(a[2])
result = int(a1 + a2 + a3)
print(result)

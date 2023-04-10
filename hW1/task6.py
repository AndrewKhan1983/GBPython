'''Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались
за проезд и получали билет с номером. Счастливым билетом называют такой билет с
шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no'''

a = input("Введите номер билета из 6 цифр: ")
a1 = int(a[0])
a2 = int(a[1])
a3 = int(a[2])
a4 = int(a[3])
a5 = int(a[4])
a6 = int(a[5])
if (a1 + a2 + a3 == a4 + a5 + a6):
    print("Yes")
else:
    print("No")
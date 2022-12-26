# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

from random import sample

# def summa (amount):
#     new_list = sample(range(1, (amount+1)*2), k=amount)
#     print(new_list)
#     sum = 0
#     for i in range(0, amount, 2):
#         sum = sum + new_list[i]
#     return sum

# sum1 = summa(int(input('Enter amount - ')))
# print(sum1)

# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# def summa (amount):
#     new_list = sample(range(1, (amount+1)*2), k=amount)
#     print(new_list)
#     sum = 1
#     for i in range(amount//2):
#         sum = new_list[i] * new_list[amount - 1 - i]
#         print(sum, " ")
#     if (amount % 2 == 1):
#         print(new_list[amount // 2])
#     return True

# outcome = summa(int(input('Enter amount - ')))
# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.

n = int(input('Enter amount - '))
a = []
i = 0
if (n == 0):
    print(n)
while n > 0:
    a.append(n % 2)
    i = i + 1
    n = n // 2
for j in range(i, 0, -1):
    print((a[j - 1]), sep='', end='')

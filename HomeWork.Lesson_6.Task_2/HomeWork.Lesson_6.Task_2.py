﻿# Вводится натуральное число X. Подсчитайте количество натуральных делителей числа X (включая 1 и само число). x ≤ 2e9 (2 миллиарда)

x = (int(input("Введите натуральное число: ")))
count = 0

if (x <= 2 * (10**9)):
    for i in range (1, x + 1):
        if x % i == 0:
            count = count + 1
    print(count)
else:
    print("Число больше 2е9!")
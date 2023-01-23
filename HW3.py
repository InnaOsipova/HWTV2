# Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?

# Воспользуемся формулой бернули

from math import factorial

# функция по расчету сочетаний
def combinations (k, n):
    return factorial(n)/(factorial(k)*factorial(n-k))

k = 70
n = 144
p = 0.5
q = 1 - p
print(f'Вероятность выпадания орла {k} раз = {round(combinations(k,n) * p ** k * q ** (n-k) * 100, 2)} %')
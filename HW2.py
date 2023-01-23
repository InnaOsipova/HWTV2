# Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004. 
# В жилом комплексе после ремонта в один день включили 5000 новых лампочек.
# Какова вероятность, что ни одна из них не перегорит в первый день? 
# Какова вероятность, что перегорят ровно две?

# т.к. вероятность маленькая, а число испытаний большое, воспользуемся формулой пуассона

from math import factorial
import math

def puasson (p, n, m):
    lam = p * n
    return ((lam ** m)/factorial(m)) * math.pow(2.72,-lam)

print(f'Вероятность что ни одна лампочка не перегорит = {round(puasson(0.0004, 5000, 0) * 100, 2)} % ')
print(f'Вероятность что перегорит 2 лампочки = {round(puasson(0.0004, 5000, 2) * 100, 2)} % ')
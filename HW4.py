# В первом ящике находится 10 мячей, из которых 7 - белые. Во втором ящике - 11 мячей, из которых 9 белых. 
# Из каждого ящика вытаскивают случайным образом по два мяча. 
# Какова вероятность того, что все мячи белые? 
# Какова вероятность того, что ровно два мяча белые? 
# Какова вероятность того, что хотя бы один мяч белый?

from math import factorial


# Нужно найти вероятность, это отношение благоприятных событий к числу всех  событий

def probability (m, n):
    return m/n

# функция по расчету сочетаний
def combinations (k, n):
    return factorial(n)/(factorial(k)*factorial(n-k))

def prob1 (k, n, m, o):
    return probability(combinations(k,m) * combinations(o-k,n-m), combinations(o, n))



# Вероятность что все мячи белые
print (f'Вероятность того, что все мячи белые = {round(probability(combinations(2,7) * combinations(0,3), combinations(2, 10))* probability(combinations(2,9) * combinations(0,2), combinations(2, 11))*100, 2)} %')


# Вероятность , что 2 мяча белые
var1 = prob1(2,10,7,2)*prob1(0,11,9,2)
var2 = prob1(0,10,7,2)*prob1(2,11,9,2)
var3 = prob1(1,10,7,2)*prob1(1,11,9,2)

print (f' Вероятность что два мяча белые  = {round((var1+var2+var3)*100, 2)} %')

# Хотябы 1 мяч белый, .е. устраивает 1 или 2 или 3 или 4
var4 = prob1(1,10,7,2)*prob1(0,11,9,2)
var5 = prob1(0,10,7,2)*prob1(1,11,9,2)
var6 = prob1(2,10,7,2)*prob1(1,11,9,2)
var7 = prob1(1,10,7,2)*prob1(2,11,9,2)
var8 = prob1(2,10,7,2)*prob1(2,11,9,2)

print (f' Вероятность что хотябы 1 мяч белый   = {round((var1+var2+var3+var4+var5+var6+var7+var8)*100, 2)} %')
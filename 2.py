# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
n = int(input('введите любое трехзначное число: '))
x = n + 0
sum = 0
while (n != 0):
    sum = sum + n % 10
    n = n // 10
print (f"{x} -> ", sum)


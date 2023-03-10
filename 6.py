# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no
tiket = list(map(int, list(input('Введите шестизначный номер билета: '))))
left = sum(tiket[0: -3]) #сумма от 0 до 3 с конца
right = sum(tiket[-3:]) #сумма последних 3 чисел
if left == right:
    print(f'{tiket} -> yes')
else:
    print(f'{tiket} -> no')




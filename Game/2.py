"""
Суть игры: ваш соперник, будь то компьютер или друг, загадывает 4-значное число, состоящее из неповторяющихся цифр.
Ваша задача - угадать его за ограниченное число ходов. В качестве подсказок выступают “коровы”
(цифра угадана, но её позиция - нет) и “быки” (когда совпадает и цифра и её позиция).
То есть если загадано число “1234”, а вы называете “6531”, то результатом будет 1 корова (цифра “1”)
и 1 бык (цифра “3”).

Чем полезно: создание игры не потребует от вас углубленного знания языка, а сам язык может быть практически любой.
При этом вам придётся использовать практически все базовые упражнения с циклами и операторами,
да и на выходе получится весьма интересная игра.

Как усложнить: сохранение результатов, круговое соревнование на несколько игроков, режим турнира, игра по сети.
for index1, i in enumerate(n):
    for index2, j in enumerate(m):
        if j == i:
            if index2 == index1:
                print(f"Yes!\n{j} is in n and it's index {index2}")
            else:
                print(f"Yes!\n{j} is in n, but you don't guessed index.")
"""
import random


def func(number):
    numberRandom = str(random.randint(1000, 10000))
    for index1, i in enumerate(numberRandom):
        for index2, j in enumerate(number):
            if j == i:
                if index2 == index1:
                    print(f"Yes!\n{j} is in random number and it's index {index2}")
                    print('------------------------------------------------------')
                else:
                    print(f"Yes!\n{j} is in random number, but you don't guessed index.\nNumber {j} has index {index1} and not {index2}")
                    print('------------------------------------------------------')


if __name__ == '__main__':
    q = True
    while q is True:
        n = str(input('Input your number, please: '))
        if len(n) > 4 or len(n) < 4:
            print("Error!\nLength your number most be 4!")
        else:
            q = False
    func(n)

# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
#  Функцию hex используйте для проверки своего результата

def conv_Number(num_Dec, ss):
    digits = "0123456789ABCDEF"          
    num_Conv = ""                          
    while (num_Dec > 0):        
        k = num_Dec % ss                    
        num_Conv = digits[k] + num_Conv     
        num_Dec = num_Dec // ss             
    return num_Conv

def Main():
    number = int(input('Число в десятичной СС: '))
    number_system = 16
    print(f'Ответ в {number_system}-ой СС = ', conv_Number(number, number_system))
    print(f'Функция hex для проверки результата {hex(number)}')

Main()


# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

import math

def sum_Fraction(number_frac_1, number_frac_2):     # Сложение дробей и приведение к НОД
    sum_frac = [int(number_frac_1[0]) * int(number_frac_2[1]) \
                       + int(number_frac_2[0]) * int(number_frac_1[1]),
                int(number_frac_1[1]) * int(number_frac_2[1])]
    nod = math.gcd(sum_frac[0], sum_frac[1]) #Наименьший общий делитель
    sum_frac = [int(sum_frac[0] / nod), int(sum_frac[1] / nod)]
    print('Cyммa дробей = ', sum_frac[0], '/', sum_frac[1])

def mult_Fraction(number_frac_1, number_frac_2):    # Умножение дробей и приведение к НОД
    mult_frac = [int(number_frac_1[0]) * int(number_frac_2[0]),
                 int(number_frac_1[1]) * int(number_frac_2[1])]
    nod = math.gcd(mult_frac[0], mult_frac[1])
    mult_frac = [int(mult_frac[0] / nod), int(mult_frac[1] / nod)]
    print('Произведение дробей = ', mult_frac[0], '/', mult_frac[1])

def Main():
    number_frac_1 = str(input('Введите первое число вида a/b - ')).split('/')
    number_frac_2 = str(input('Введите второе число вида a/b - ')).split('/')
    sum_Fraction(number_frac_1, number_frac_2)
    mult_Fraction(number_frac_1, number_frac_2)

Main()


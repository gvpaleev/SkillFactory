"""
    04.03.2021г.
    Палеев Геннадий Владимирович 
    gv.paleev@gmail.com
    ____________________________

    Программа по отгадыванию загаданного числа от 1 до 100.

"""
import numpy as np


def game_core(number):
    '''Заводим переменные начала и конца интервала.
        Каждый цикл позволит сузить интервал в 2 раза,
        предполагаемое число — это округленная медиана интервала.
    '''
    begin_interval = 1
    end_interval = 101
    median_interval = 50

    count = 0

    while number != median_interval:

        count+=1

        if number > median_interval: 
            # Объязательно инкремент для исключения медианы из сл. выборки
            begin_interval = median_interval+1

        elif number < median_interval:
            end_interval = median_interval

        median_interval = int(np.median([ x for x in range(begin_interval,end_interval)]))


    return(count)




def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''

    np.random.seed(1) 

    count_ls = []
    random_array = np.random.randint(1,101, size=(1000))

    for number in random_array:
        count_ls.append(game_core(number))

    score = int(np.mean(count_ls))

    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    
    return(score)

# запускаем
score_game(game_core)
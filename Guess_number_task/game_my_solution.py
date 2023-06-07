"""Игра угадай число
Компьютер сам загадывает и сам угадывает число по заданному нами алгоритму
"""

import numpy as np


def game_rational_predict_v3(number: int = 1) -> int:
    """ Сначала устанавливаем число 50, а потом увечиваем либо уменьшаем его,
    если число больше или меньше нужного
    Args:
        number (int, optional): Загаданное число. Defaults to 1.
    Returns:
        int: Число попыток
    """
    count = 0
    predict = 50
    while number != predict:
        count += 1
        corrector = 50 // 2**count + 1  # Поправка для предполагаемого числа
        if number > predict:
            predict += corrector
        elif number < predict:
            predict -= corrector

    return count


def score_game(game_rational_predict_v3) -> int:
    """ЗА какое количство попыток в среднем за 1000 подходов
    угадывает наш алгоритм
    Args:
        game_core_v3 ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # список чисел

    for number in random_array:
        count_ls.append(game_rational_predict_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попытки")
    return score


if __name__ == "__main__":
    # RUN
    score_game(game_rational_predict_v3)

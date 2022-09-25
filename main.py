# база слов, которая участвует в программе
from typing import List
import random

words = [
    "Яблоко",
    "Малина",
    "Апельсин"
]


word = random.choice(words)
guessed_letters_indexes = []


def get_input_letter() -> str:
    """
        Функция которая берет букву из стандартного потока
        (input('введите букву')) и возвращяет ее
    """
    # print('Введите букву:')
    letter = str(input('Введите букву: '))
    return letter


def check_letter(letter: str, word: str) -> List[int]:
    """
        Функция которая проверяет есть ли буква letter в слове word,
        если есть - возвращяет список индексов, если нет - возвращяет пустой список
    """
    indexes = []
    for index, iter_letter in enumerate(word):
        if iter_letter == letter:
            indexes.append(index)
    guessed_letters_indexes.append(indexes)
    return indexes


def display_word(guessed_letters_indexes: List[int], word: str):
    """
        Формирует строку вида Я_ло_о (неугаданные буквы заменить _)
        и отображает в стандартном потоке вывода (print())
    """
    displayword = list(word)
    for i in range(len(word)):
        if i not in guessed_letters_indexes:
            displayword[i] = "_"
    print(*displayword, sep='')


def check_end_game(guessed_letters_indexes: List[int], word: str) -> bool:
    """
        Проверяет окончена ли игра: если guessed_letter_indexes формируют в итоге слово word, то игра заканчивается
    """
    end_game = True
    for i in range(len(word)):
        if i not in guessed_letters_indexes:
            end_game = False
    return end_game


def main():
    """
    Функция логики игры, будет состоять из последовательного вызова функций:
    0) Инициализация игры - выбрать рандомно слово из массива words - слово которое будем отгадывать
    1) Сначала надо спросить у игрока букву (get_input_letter)
    2) Потом проверить букву: есть ли она в слове (check_letter)
    3) Отобразить текущее состояние слова (display_word)
    4) Проверить - окончена ли игра (check_end_gamy)
    5) Если игра не окончена - выполнять сначала
    """
    while not check_end_game(guessed_letters_indexes, word):
        letter = get_input_letter()
        guessed_letters_indexes.extend(check_letter(letter, word))
        display_word(guessed_letters_indexes, word)
    print("You`re right")


if __name__ == '__main__':
    main()

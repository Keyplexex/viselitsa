from typing import List

class View:
    def get_input_letter(self) -> str:
        """
        Содержимое функции взять из main.py
        """

        letter = str(input('Введите букву: '))
        return letter

    def display_word(guessed_letters_indexes: List[int], word: str) -> None:
        """
        Содержимое функции взять из main.py
        """
        displayword = list(word)
        for i in range(len(word)):
            if i not in guessed_letters_indexes:
                displayword[i] = "_"
        print(*displayword, sep='')
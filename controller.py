class Controller:
    def __init__(self, word):
        """
        Функция начала игры. Вся логика этой функции заключается в инициализации пространства имен
        ()
        (https://docs.python.org/3/tutorial/classes.html)
        """
        self.word = word
        self.guessed_word_indexes = []

    def check_letter(self, letter, word, guessed_letters_indexes):
        """
        Перенести логику из main.py
        """
        indexes = []
        for index, iter_letter in enumerate(word):
            if iter_letter == letter:
                indexes.append(index)
        guessed_letters_indexes.append(indexes)
        return indexes

    def check_end_game(self, word, guessed_letters_indexes):
        """
        Перенести логику из main.py
        """
        end_game = True
        for i in range(len(word)):
            if i not in guessed_letters_indexes:
                end_game = False
        return end_game

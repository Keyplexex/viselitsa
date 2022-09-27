import random


class Model:
    # Заполнить список слов
    words = ['яблоко', 'апельсин', 'картошка', 'тотошка']

    def get_random_word(self, words) -> str:
        """Сгенерировать рандомное слово из массива self.words"""
        random_word = random.choice(words)
        return random_word

# word_generator.py
from json import load
from unidecode import unidecode
from random import choice

class Word:
    def __init__(self, tema):
        with open(f'./files/{tema}.json', 'r', encoding='utf-8') as file:
            self.words_grouped = load(file)

    def palavradificuldade(self, dificuldade):
        dificuldade = int(dificuldade)
        if dificuldade == 1:
            words = self.words_grouped.get('1', [])
        elif dificuldade == 2:
            words = self.words_grouped.get('2', [])
        elif dificuldade == 3:
            words = self.words_grouped.get('3', [])
        else:
            words = []
        
        chosen_word = choice(words).lower()
        return unidecode(chosen_word)

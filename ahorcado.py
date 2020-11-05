import random

IMAGES = ['''
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\  |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\  |
    /    |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\  |
    / \  |
        |
    =========''']

PALABRAS = [
    'esternocleidomaistoideo'
    'electroencefalograma'
    'gato'
    'rayo'
    'cuchillo'
    'mesa'
    'silla'
    'hamster'
    'canario'
    'tijera'
]

def random_word():
    index = random.randint(0, len(PALABRAS)-1)
    return PALABRAS[index]

def run():
    word = random_word()
    hidden_word= ['-'] * len(word)
    pass

if __name__ == '__main__':
    print('¡ B I E N V E N I D O !')
    run()
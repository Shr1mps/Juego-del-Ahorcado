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
    'esternocleidomaistoideo',
    'electroencefalograma',
    'gato',
    'rayo',
    'cuchillo',
    'mesa',
    'silla',
    'hamster',
    'canario',
    'tijera'
]

def random_word():
    index = random.randint(0, len(PALABRAS)-1)
    return PALABRAS[index]

def display(Hword, attempts):
    print(IMAGES[attempts])
    print(' ')
    print(Hword)
    print('.-.-.-.-.-.-.-.-.-.')




def run():
    word = random_word()
    Hword= ['-'] * len(word)
    attempts= 0

    while True:
        display(Hword, attempts)
        letra= str(input('Escoge una letra:'))

if __name__ == '__main__':
    print('¡ B I E N V E N I D O !')
    run()
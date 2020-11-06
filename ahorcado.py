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
        index_letras=[]
        letra= str(input('Escoge una letra:'))
        for i in range (len(word)):
            if word[i] == letra:
                index_letras.append(i)
        if len(index_letras) == 0:
            attempts += 1

            if attempts == 7:
                display(Hword, attempts)
                print('')
                print('¡Perdiste! La palabra correcta era {}'.format(word))
                break
        else:
            for i in index_letras:
                Hword[i] = letra

            index_letras = []

        try:
            Hword.index('-')
        except ValueError:
            print('')
            print('¡Felicidades! Ganaste. La palabra es: {}'.format(word))
            break


if __name__ == '__main__':
    print('¡ B I E N V E N I D O !')
    run()
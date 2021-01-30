from random import randint

def random_square():
    """returns a tuple (coords, color)"""
    rank = randint(1, 8)
    filenum = randint(1, 8)
    color = 'Dark'
    if (rank + filenum) % 2:
        color = 'Light'

    return f'{chr(filenum + 96)}{rank}', color
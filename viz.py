from random import randint
import time

answer = None

fs = int(ord(input('file start? ')) - 96)
fe = int(ord(input('file end? ')) - 96)
rs = int(input('rank start? '))
re = int(input('rank end? '))

score = 0
start_time = time.time()
while not answer == 'q':
    rank = randint(rs, re)
    filenum = randint(fs, fe)
    color = 'b'
    if (rank + filenum) % 2:
        color = 'w'
    answer = input(f'{chr(filenum + 96)}{rank} color? ')
    if answer == color:
        print('correct!')
        score += 1
    else:
        print(f'game over. score: {score}')
        elapsed_time = time.time() - start_time
        print(f'average time per answer: {elapsed_time / score}')
        quit()

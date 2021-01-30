import clipboard
from chesso import random_square

pause_duration = 3000
output = ''

for _ in range(1000):
    sq, color = random_square()
    output += f'{sq} [[slnc {pause_duration}]] {color} [[slnc 1500]]\n'

clipboard.copy(output)

print('copied to clipboard')
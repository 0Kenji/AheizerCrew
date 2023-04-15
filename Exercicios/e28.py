#incompleto
import random
num = random.randint(0,5)
num1: int(input('Tente acertar o número: '))
if num1 == num:
    print('Parabéns')
else:
    print('Errado')
from math import sqrt, floor
import random
num = random.randint(1, 100)
raiz = sqrt(num)
print('A raiz de {} é igual a {:.3f}'.format(num, floor(raiz)))
n1 = int(input('Um valor'))
n2 = int(input('Outro'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}, o produto é {:.3f} e a divisão é {}'.format(s, m, d), end= '>>>')
print('Divisão inteira {} e a potência {}'.format(di, e))

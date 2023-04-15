v = list()
for cont in range(0, 5):
    v.append(int(input('Digite um valor: ')))

for c, n in enumerate(v):
    print('Na posição {} encontrei o valor {}! '.format(c, n))
print('Cheguei ao final da lista')

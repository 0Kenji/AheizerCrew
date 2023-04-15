nome = str(input('Digite seu nome: '))
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m'}
print('Olá. Muito prazer em te conhecer, {}{}{}!!'.format(cores['azul'], nome, cores['amarelo']))

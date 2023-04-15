salário = float(input('Digite o salário: R$ '))
if salário >= 1250.00:
    aumento = salário + (salário * 10 / 100)
    print('O salário terá o valor de {}'.format(aumento))
    print('Aumentou 10%')
else:
    aumento2 = salário + (salário * 15 / 100)
    print('O salarío terá o valor de {}'.format(aumento2))
    print('Aumentou 15%')

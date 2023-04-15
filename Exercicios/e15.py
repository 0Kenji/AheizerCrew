km = float(input('Quantos quilometros percorridos? : KM'))
dia = int(input('O carro foi alugado por quantos dias? '))
preço1 = (km * 0.15)
preço2 = (dia * 60)
total = preço1 + preço2
print('O preço final foi R${}'.format(total))

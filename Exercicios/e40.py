#incompleto
n1 = float(input('Qual foi a primeira nota?: '))
n2 = float(input('Qual foi a segunda nota?: '))
media = (n1 * n2 / 2)
if media <= 5.0:
    print('Você foi reprovado')
elif media >= 7.0:
    print('Você foi aprovado')
print()

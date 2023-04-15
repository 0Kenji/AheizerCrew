nome = str(input('Qual o seu nome?: '))
if nome == 'Bianca':
    print('Que nome bonito!')
elif nome == 'Paulo' or nome == 'Maria' or nome == 'Gabriel':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Julia Juliana Marcia Maria':
    print('Belo nome feminino')
elif nome in 'Pedro Julio Mario':
    print('Belo nome masculino')
else:
    print('Nome estranho')
print('Tenha um bom dia! {}'.format(nome))

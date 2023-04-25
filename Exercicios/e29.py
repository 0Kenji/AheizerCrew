v = float(input ('Qual é a sua velocidade atual?'))
if  v <=80:
    print ('Sua velocidade está na média, siga!')
else:
    print ('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    print ('Você deve pagar uma multa de R${}'.format((v-80)*7))
print('Tenha um bom dia!Dirija com segurança!')
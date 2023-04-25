def somar(a = 0, b = 0, c = 0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    """
    s = a + b + c
    return(s)


r1 = somar(3, 2, 5)
r2 = somar(8, 4)
r3 = somar(b = 4, c = 3)

print(f'Os resultados foram {r1}, {r2} e {r3}')
#help(somar)
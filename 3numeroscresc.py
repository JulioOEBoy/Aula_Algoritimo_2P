contador = 0

while contador < 3:
    print('Digite 3 numeros e mostrarei em ordem decrescente')
    numero = float(input('Digite um numero: '))
    if contador == 0:
        n1 = numero
    if contador == 1:
        n2 = numero
    else:
        n3 = numero
    contador += 1
print(f'Os numeros em ordem decrescente são: {sorted([n1, n2, n3], reverse=True)}')
print('Fim')
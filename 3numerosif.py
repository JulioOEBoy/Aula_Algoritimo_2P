contador = 0

while contador < 3:
    print(['Diga 3 numeros e direi qual é o maior'])
    numero = float(input('Digite um numero: '))
    if contador == 0:
        maior = numero
    if numero > maior:
        maior = numero
    contador += 1
print(f'O maior numero é {maior}')
print('Fim')
#!/usr/bin/env python3

# Escreva um programa que leia dois números. Imprima a multiplicação do primeiro 
# pelo segundo. Utilize somente os operadores de soma e subtração para calcular o resultado.
# Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas 
# de um deles. Assim, 4 * 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.

x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))
z = 1
soma = 0

while z <= y:
    soma = soma + x    
    if z == y:
        print(f'O resultado é = {soma}')
    z = z + 1

    

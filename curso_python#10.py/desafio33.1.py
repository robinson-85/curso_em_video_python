''' Faça um programa que leia três números
e mostre qual é o maior e o menor número '''

import sys

try:
    a = int(input("Primeiro valor: "))
except Exception as error:
    print("Você deve informar apenas números")
    sys.exit()

try:
    b = int(input("Segundo valor: "))
except Exception as error:
    print("Você deve informar apenas números")
    sys.exit()

try:
    c = int(input("Terceiro valor: "))
except Exception as error:
    print("Você deve informar apenas números")
    sys.exit()

# verificando quem é menor
menor = a 
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print("O menor valor digitado foi {}".format(menor))
print("O maior valor digitado foi {}".format(maior))


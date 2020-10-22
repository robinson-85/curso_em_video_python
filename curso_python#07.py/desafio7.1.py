''' 7. Desenvolva um programa que leia as duas notas de um aluno, calcule 
e mostre a sua média. '''

import sys

try:
    n1 = float(input("Primeira nota do aluno: "))
except Exception as error:
    print("Voce deve informar apenas numeros")
    sys.exit()

try:
    n2 = float(input("Segunda nota do aluno: "))
except Exception as error:
    print("Voce deve informar apenas numeros")
    sys.exit()

media = (n1 + n2) / 2
print("A média entre {:.1f} e {:.1f} é igual a {:.1f}".format(n1, n2, media))
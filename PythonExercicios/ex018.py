'''18 Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,cosseno e tangente
desse ângulo'''
from math import cos,sin,tan,radians
a = float(input('Digite um ângulo qualquer: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('O ângulo de {} tem o "seno" de {:.3f} \nO ângulo de {} tem o "cosseno" de {:.3f} \n'
      'O ângulo de {} tem a "tangente" de {:.3f}'.format(a, s, a, c, a, t))

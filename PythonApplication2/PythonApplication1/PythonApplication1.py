# Bibliotecas Adicionais
import numpy as np
from sympy import Symbol
import sympy as sym

# Definição dos arrays

print("Interpolador Polinomial: ")
qtd= int(input("Digite quantos valores de X serão digitados: "))
X = list()
print("========================")
print("============ Digite Valores para X ============")
for cont in range(0,qtd):
    X.append(float(input('Digite um valor para X:  ')))
print("========================")
print("============ Digite Valores para os FX correspondentes ============")
FX= list()
for CONT in range(0,qtd):
    FX.append(float(input('Digite um valor para FX:  ')))

x=Symbol('x')
arraylen= len(X)
L=[]

#Primeiro loop para determinar numerador e denominador
for i in range(arraylen):
        arrayaux= np.arange(arraylen)
        arrayaux= list(arrayaux)
        arrayaux.remove(i)
        numLi=1
        denLi=1

# Segundo loop para realizar as divisões sucetivas
        for j in arrayaux:
            numLi=numLi * (x - X[j])
            denLi = denLi* (X[i]-X[j])
        Li=numLi/denLi
        L.append(sym.expand(Li))

# Teorema de Lagrange Explicito e print na tela 
p= np.sum(FX*np.array(L))
print("========================")
print("Polinomio Interpolador: ")
print(p)
print("========================")


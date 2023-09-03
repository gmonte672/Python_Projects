import math
def f(x): 
    return (pow(x,5))-(10/9)*(pow(x,3))+(5/21)*(x)
def metodoSecante():
    X0=float(input("Digite o X0  "))
    X1=float(input("Digite o X1  "))
    iteracoes= int( input("Digite o Max de iterações  "))
    iteracao=0
    while iteracao<=iteracoes:
        X2= ( X0*f(X1)-X1*f(X0) ) / (f(X1)-f(X0))
        X0=X1
        X1=X2
        iteracao+=1
        print("A raiz encontrada de X foi ",X2)
        print("f(x2) ",f(X2))
input(metodoSecante())
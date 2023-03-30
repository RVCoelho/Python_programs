#from sklearn.linear_model import LinearRegression
import math
import statistics

n=float(input("Digite o valor para n: "))

somaXY=16345.46
somaX2=79.68
somaY2=3412308.32
somaX=math.sqrt(somaX2)
somaY=math.sqrt(somaY2)

numerador= n*somaXY - somaX*somaY
denominador=math.sqrt(abs(n*somaX2 - (somaX)**2))*math.sqrt(abs(n*somaX2 - (somaY)**2))

r=numerador/denominador

print("r:",round(r,2))

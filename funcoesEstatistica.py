# Arquivo: RicardoCoelho_AD_av1_ex1b
# Autor: Ricardo Veiga Coelho
# TIA: 42241588
# Data: 31/08/22
# Descrição: Avaliação Continuada 1 – Análise exploratória dos dados. - exercicio 1 item b

import statistics
import numpy
from matplotlib import pyplot as plt 
import pandas as pd
import math

vetor=[5,2,7,4,2,8,9,2,1,6,7,10,0,5,4,2,7,6,4,8,2]
print(vetor)

print("\nMédia:",round(statistics.mean(vetor),2))
print("\nMediana:",round(statistics.median(vetor),2))
print("\nVariância",round(statistics.variance(vetor),2))
print("\nDesvio padrão:",round(statistics.stdev(vetor),2))
Desv=math.sqrt(statistics.variance(vetor))
Coef=str(round((Desv/statistics.mean(vetor)*100),2))
print("\nCoeficiende de variação do conjunto: "+Coef+"%\n")

print("\n1º Quartil:",numpy.quantile(vetor,[0.25]))
print("\n3º Quartil:",numpy.quantile(vetor,[0.75]))

numpy.histogram(vetor,bins = [0,20,40,60,80,100])
bins = numpy.histogram(vetor,bins = [0,20,40,60,80,100])
vetor=numpy.array([5,2,7,4,2,8,9,2,1,6,7,10,0,5,4,2,7,6,4,8,2])
plt.hist(vetor, bins = [0,1,2,3,4,5,6,7,8,9,10]) 
plt.title("histograma") 
plt.show()

#plt.boxplot(vetor)
#plt.show()

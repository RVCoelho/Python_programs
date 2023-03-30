# Arquivo: RicardoCoelho_AD_av1_ex1c
# Autor: Ricardo Veiga Coelho
# TIA: 42241588
# Data: 28/08/22
# Descrição: Avaliação Continuada 1 – Análise exploratória dos dados. - exercicio 1 item c

import math

def media(lista):
  #divide a soma de todos pelo numero de elementos no conjunto
  Media = sum(lista)/len(lista)
  return Media

def mediana(lista):
  lista.sort()# deve-se ordenar a lista em ordem crescente para poder achar a mediana
  #print(lista)
# tamanho impar (mediana é o elemento central do conjunto)
  if len(lista)%2==0: 
    centro=(len(lista)/2)+1
# tamanho par (neste caso a mediana é a média dos dois elementos centrais)
  else:
    centro=(len(lista)/2+(len(lista)/2)+1)/2
  return lista[int(centro)]

def variancia(lista):
  Media=media(lista)
  Variancia=sum((x - Media) ** 2 for x in lista) / (len(lista)-1)
  return Variancia

def coefVariacao(lista):
  desvPadrao=math.sqrt(variancia(lista))
  x=media(lista)
  Coef=(desvPadrao/x)*100 #multiplicado por 100 pois o valor está em porcentagem!
  return Coef

def quartil1(lista):
  lista.sort()
  i=0
  metade1=[]
  while i < mediana(lista):
    metade1.append(lista[i])
    i+=1
  return mediana(metade1)
  
def quartil3(lista):
  lista.sort()
  i=len(lista)-1
  metade2=[]
  while i > mediana(lista):
    metade2.append(lista[i])
    i-=1
  return mediana(metade2)

#main
vetor=[5,2,7,4,2,8,9,2,1,6,7,10,0,5,4,2,7,6,4,8,2]
print(vetor)

#calculo da média
calculo=str(round(media(vetor),2))
print("\nMédia do conjunto: "+calculo+"\n")

#calculo da mediana
calculo=str(round(mediana(vetor),2))
print("Mediana do conjunto: "+calculo+"\n")

#calculo da moda
#moda(vetor)

#calculo da variância
calculo=str(round(variancia(vetor),2))
print("Variância do conjunto: "+calculo+"\n")

#calculo do desvio-padrão (basta fazer a raiz quadrada da variância)
calculo=str(round(math.sqrt(variancia(vetor)),2))
print("Desvio-padrão do conjunto: "+calculo+"\n")

#calculo do coeficiente de variação
calculo=str(round(coefVariacao(vetor),2))
print("Coeficiende de variação do conjunto: "+calculo+"%\n")

#calculo dos quartis
#1º quartil
calculo=str(round(quartil1(vetor),2))
print("1º quartil do conjunto: "+calculo+"\n")
#3º quartil
calculo=str(round(quartil3(vetor),2))
print("3º quartil do conjunto: "+calculo+"\n")

###### EXERCÍCIO 1
def media (nota1,nota2):
    med = (nota1 + nota2)/2
    return(med)
"""TESTE:
m = media(1,2)
print(m)
"""
"""
#PARA ANALISAR OS EPISÓDIOS
with open ('series.csv', 'r', encoding = 'utf-8') as file:
    for line in file.readlines():
        separado = line.split(',')
        print(separado[2])
"""

###### EXERCÍCIO 2
import csv
with open('series.csv', 'r') as f:
  reader = csv.reader(f)
  lista = list(reader)
with open('series_novas.csv','r') as g:
    read = csv.reader(g)
    lista2 = list(read)
listafinal = lista + lista2 #combinar as duas listas em uma só
######EXERCÍCIO 3
eps = 0 #total de eps
x = len(listafinal)
contador =0
for h in range (1,x) :
    y = 0
    l = 0
    if listafinal[y] == listafinal[l]:
        l = l+7
    """
print(x)
linhas = int(x / 7)
for k in range (1,linhas):
    print(listafinal[0][3])
    """
####EXERCÍCIO 4
"""
dicio = {}
nome = listafinal[0]
n1 = listafinal[5]
n2 = listafinal[6]
dicio[listafinal[0]] = media(listafinal[5].listafinal[6])
"""
###EXERCÍCIO 5
for h in range (1,x):
    if listafinal[0] == "Narcos":
        for i in range (1,7):
            listafinal.pop(lista[i-1])



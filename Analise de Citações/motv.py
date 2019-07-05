# libraries
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
from scipy import *

# definindo os dados de publico alvo, metodologias e qtd de citações

#array para manipular o z
array_sum = []

#Definindo motivação e estudo de caso / SOMATORIO das citações por grupo
x_sum = ('ABP','ABP','ABP','ABP','ABP','ABP','C','C','C','C','C','C','C/DT','C/DT','C/DT','C/DT','C/DT','C/DT','CT/DT','CT/DT','CT/DT','CT/DT','CT/DT','CT/DT','CT','CT','CT','CT','CT','CT','DD','DD','DD','DD','DD','DD','DT','DT','DT','DT','DT','DT','ID','ID','ID','ID','ID','ID','LB','LB','LB','LB','LB','LB','N/D','N/D','N/D','N/D','N/D','N/D','PBL','PBL','PBL','PBL','PBL','PBL','PC','PC','PC','PC','PC','PC','PS','PS','PS','PS','PS','PS')
y_sum = ('CKR','DE','DEXP','EC','ER','RL','CKR','DE','DEXP','EC','ER','RL','CKR','DE','DEXP','EC','ER','RL','CKR','DE','DEXP','EC','ER','RL','CKR','DE','DEXP','EC','ER','RL','CKR','DE','DEXP','EC','ER','RL','CKR','DE','DEXP','EC','ER','RL','CKR','DE','DEXP','EC','ER','RL','CKR','DE','DEXP','EC','ER','RL','CKR','DE','DEXP','EC','ER','RL','CKR','DE','DEXP','EC','ER','RL','CKR','DE','DEXP','EC','ER','RL','CKR','DE','DEXP','EC','ER','RL')
z_sum = (0,0,7,0,0,0,23,12,18,6,6,0,0,0,0,0,4,0,0,0,2,0,101,0,18,24,269,2,8,0,0,0,2,0,0,0,0,0,0,0,49,0,0,0,1,0,0,0,43,10,22,0,0,0,0,5,68,0,0,0,0,0,0,0,6,0,0,2,0,0,4,11,0,0,12,0,1,0)

for i in range(len(y_sum)):
    array_sum.append((z_sum[i]))
    #if para checar as linhas que possuem 0 e evitar que sejam printadas no gráfico
    if array_sum[i]>0:
       text(x_sum[i], y_sum[i],
       array_sum[i],size=10, horizontalalignment='center',verticalalignment='center')


teste = []
for i in range(77):
   teste.append((array_sum[i])*20)


plt.scatter(x_sum,y_sum,s=teste,c='red', alpha=0.5)
#plt.show()
plt.savefig('motivacaoporestudo.pdf')
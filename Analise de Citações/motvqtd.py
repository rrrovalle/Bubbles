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
z_sum = (0,0,2,0,0,0,2,1,5,1,1,0,0,0,0,0,1,0,0,0,1,0,8,0,3,3,40,1,4,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,5,4,7,0,0,0,0,2,3,0,0,0,0,0,0,0,1,0,0,1,0,0,1,4,0,0,1,0,1,0)

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
plt.savefig('motivacaoporestudoqtd.pdf')
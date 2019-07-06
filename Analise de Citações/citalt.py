# libraries
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
from scipy import *

# definindo os dados de publico alvo, metodologias e qtd de citações

#array para manipular o z
array_sum = []


#somatorio de cada topico
x_sum = ('P','P','P','P','P','P','P','P','P','P','P','P','P','P','P','P','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','M','M','M','M','M','M','M','M','M','M','M','M','M','M','M','M','S','S','S','S','S','S','S','S','S','S','S','S','S','S','S','S','F/M','F/M','F/M','F/M','F/M','F/M','F/M','F/M','F/M','F/M','F/M','F/M','F/M','F/M','F/M','F/M','F/S','F/S','F/S','F/S','F/S','F/S','F/S','F/S','F/S','F/S','F/S','F/S','F/S','F/S','F/S','F/S','M/T','M/T','M/T','M/T','M/T','M/T','M/T','M/T','M/T','M/T','M/T','M/T','M/T','M/T','M/T','M/T','F/M/S','F/M/S','F/M/S','F/M/S','F/M/S','F/M/S','F/M/S','F/M/S','F/M/S','F/M/S','F/M/S','F/M/S','F/M/S','F/M/S','F/M/S','F/M/S','M/T/S','M/T/S','M/T/S','M/T/S','M/T/S','M/T/S','M/T/S','M/T/S','M/T/S','M/T/S','M/T/S','M/T/S','M/T/S','M/T/S','M/T/S','M/T/S','G','G','G','G','G','G','G','G','G','G','G','G','G','G','G','G','N/D','N/D','N/D','N/D','N/D','N/D','N/D','N/D','N/D','N/D','N/D','N/D','N/D','N/D','N/D','N/D')
y_sum = ('ABP','C','C/DT','CT','CT/DT','DD','DT','ID','LB','MC','N/D','PBL','PC','PS','RF','RL','ABP','C','C/DT','CT','CT/DT','DD','DT','ID','LB','MC','N/D','PBL','PC','PS','RF','RL','ABP','C','C/DT','CT','CT/DT','DD','DT','ID','LB','MC','N/D','PBL','PC','PS','RF','RL','ABP','C','C/DT','CT','CT/DT','DD','DT','ID','LB','MC','N/D','PBL','PC','PS','RF','RL','ABP','C','C/DT','CT','CT/DT','DD','DT','ID','LB','MC','N/D','PBL','PC','PS','RF','RL','ABP','C','C/DT','CT','CT/DT','DD','DT','ID','LB','MC','N/D','PBL','PC','PS','RF','RL','ABP','C','C/DT','CT','CT/DT','DD','DT','ID','LB','MC','N/D','PBL','PC','PS','RF','RL','ABP','C','C/DT','CT','CT/DT','DD','DT','ID','LB','MC','N/D','PBL','PC','PS','RF','RL','ABP','C','C/DT','CT','CT/DT','DD','DT','ID','LB','MC','N/D','PBL','PC','PS','RF','RL','ABP','C','C/DT','CT','CT/DT','DD','DT','ID','LB','MC','N/D','PBL','PC','PS','RF','RL','ABP','C','C/DT','CT','CT/DT','DD','DT','ID','LB','MC','N/D','PBL','PC','PS','RF','RL')
z_sum = (0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,13,1,0,1,0,1,0,1,0,0,0,1,0, 0,1,1,8,2,0,0,0,1,1,3,0,1,1,0,0,1,1,0,7,3,1,0,0,0,0,1,1,0,1,1,1, 0,2,0,5,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0, 1,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0, 0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,12,1,0,0,0,13,0,0,0,4,0,0,1, 0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0)

for i in range(len(y_sum)):
    array_sum.append((z_sum[i]))
    #if para checar as linhas que possuem 0 e evitar que sejam printadas no gráfico
    if array_sum[i]>0:
        text(x_sum[i], y_sum[i],
        z_sum[i],size=10, horizontalalignment='center',verticalalignment='center')


teste = []
for i in range(175):
    teste.append((array_sum[i])*60)

plt.scatter(x_sum,y_sum,s=teste,c='red', alpha=0.5)
plt.ylabel('Teorias de Aprendizagem', fontsize=15)
plt.xlabel('Público-Alvo', fontsize=15)
plt.grid()
#plt.show()


plt.savefig('PAVSTEART.pdf')



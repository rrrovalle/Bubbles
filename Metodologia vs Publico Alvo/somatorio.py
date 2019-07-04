# libraries
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
from scipy import *

# definindo os dados de publico alvo, metodologias e qtd de citações

#array para manipular o z
array_sum = [175]


#somatorio de cada topico
x_sum = ('F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F','F/M','F/M','F/M','F/M','F/M','F/M','F/M','F/M','F/M','F/M','F/M','F/M','F/M','F/M','F/M','F/M','F/M/S','F/M/S','F/M/S','F/M/S','F/M/S','F/M/S','F/M/S','F/M/S','F/M/S','F/M/S','F/M/S','F/M/S','F/M/S','F/M/S','F/M/S','F/M/S','F/S','F/S','F/S','F/S','F/S','F/S','F/S','F/S','F/S','F/S','F/S','F/S','F/S','F/S','F/S','G','G','G','G','G','G','G','G','G','G','G','G','G','G','G','G','M','M','M','M','M','M','M','M','M','M','M','M','M','M','M','M','M/T','M/T','M/T','M/T','M/T','M/T','M/T','M/T','M/T','M/T','M/T','M/T','M/T','M/T','M/T','M/T','M/T/S','M/T/S','M/T/S','M/T/S','M/T/S','M/T/S','M/T/S','M/T/S','M/T/S','M/T/S','M/T/S','M/T/S','M/T/S','M/T/S','M/T/S','M/T/S','N/D','N/D','N/D','N/D','N/D','N/D','N/D','N/D','N/D','N/D','N/D','N/D','N/D','N/D','N/D','N/D','P','P','P','P','P','P','P','P','P','P','P','P','P','P','P','P','S','S','S','S','S','S','S','S','S','S','S','S','S','S','S','S','S')
y_sum = ('ABP','C','C/DT','CT','CT/DT','DD','DT','ID','LB','MC','N/D','PBL','PC','PS','RF','RL','ABP','C','C/DT','CT','CT/DT','DD','DT','ID','LB','MC','N/D','PBL','PC','PS','RF','RL','ABP','C','C/DT','CT','CT/DT','DD','DT','ID','LB','MC','N/D','PBL','PC','PS','RF','RL','ABP','C','C/DT','CT','CT/DT','DD','DT','ID','LB','MC','N/D','PBL','PC','PS','RF','RL','ABP','C','C/DT','CT','CT/DT','DD','DT','ID','LB','MC','N/D','PBL','PC','PS','RF','RL','ABP','C','C/DT','CT','CT/DT','DD','DT','ID','LB','MC','N/D','PBL','PC','PS','RF','RL','ABP','C','C/DT','CT','CT/DT','DD','DT','ID','LB','MC','N/D','PBL','PC','PS','RF','RL','ABP','C','C/DT','CT','CT/DT','DD','DT','ID','LB','MC','N/D','PBL','PC','PS','RF','RL','ABP','C','C/DT','CT','CT/DT','DD','DT','ID','LB','MC','N/D','PBL','PC','PS','RF','RL','ABP','C','C/DT','CT','CT/DT','DD','DT','ID','LB','MC','N/D','PBL','PC','PS','RF','RL','ABP','C','C/DT','CT','CT/DT','DD','DT','ID','LB','MC','N/D','PBL','PC','PS','RF','RL')
z_sum = (0,6,0,76,43,0,49,0,2,0,3,0,0,0,4,0,0,5,0,17,9,0,0,1,0,0,0,0,4,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,41,0,65,3,0,0,0,65,0,0,0,9,0,0,13,0,7,4,36,22,0,0,0,6,1,68,0,4,1,0,0,4,0,0,15,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,3,6,0,88,18,2,0,0,0,0,2,6,0,12,0,0)

for i in range(175):
   array_sum.append((z_sum[i]))
   text(x_sum[i], y_sum[i],
        array_sum[i],size=11, horizontalalignment='center')


teste = [175]
for i in range(175):
    teste.append((z_sum[i])*25)

plt.scatter(x_sum,y_sum,s=teste,c='red', alpha=0.5)
plt.show()
#plt.savefig('citapavsteoria.pdf')






#OUTRA COISA/ ESSE SERIA O DE MOTV VS ESTUDO DE CASO

#Definindo motivação e estudo de caso
#ys = ('DEXP','ER','ER','DEXP','DEXP','CKR','ER','CKR','CKR','CKR','DE','DEXP','DEXP','DEXP','DEXP','DEXP','DEXP','DEXP','DEXP','DE','ER','DEXP','DEXP','DEXP','DEXP','ER','DEXP','DE','ER','CKR','DEXP','DEXP','DEXP','DEXP','EC','ER','DEXP','DE','DEXP','ER','DEXP','DEXP','ER','DEXP','RL','ER','DEXP','DEXP','DEXP','DEXP','DEXP','DEXP','DEXP','DEXP','DEXP','DEXP','ER','RL','DE','ER','DEXP','DEXP','ER','CKR','DEXP','ER','RL','RL','DE','DEXP','DE','CKR','DEXP','ER','DEXP','EC','DEXP','DEXP','ER','DEXP','DEXP','DEXP','DEXP','DEXP','DEXP','DEXP','DE','DEXP','DEXP','DEXP','DEXP','DEXP','DEXP','CKR','DE','DEXP','DE','DEXP','DEXP','CKR','DEXP','ER','DEXP','ER','DEXP','DE','DEXP','DEXP','CKR')
#xs = ('DS','RE','RE','RE','RE','EXP','RE','EXP','EXP','AR','DS','AR','AR','DS','EXP','EXP','DS','AR','AR','DS','RE','AR','AR','DS','AR','RE','RL','DS','AR','EXP','DS','AR','AR','EXP','TC','EXP','AR','DS','AR','EXP','AR','TC','RE','DS','EXP','DS','AR','AR','DS','RE','AR','EXP','EXP','EXP','AR','AR','RE','EXP','DS','AR','AR','DS','RE','EXP','AR','RE','EXP','EXP','DS','AR','EXP','DS','AR','AR','AR','AR','DS','AR','RE','RE','AR','DS','RE','AR','RE','AR','DS','DS','DS','DS','AR','TC','EXP','EXP','EXP','AR','DS','DS','DS','EXP','AR','AR','AR','EXP','CR','CR','AR','AR','AR')
#zs = (51,49,43,43,30,21,19,17,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,9,9,9,8,8,8,8,7,7,6,6,6,6,6,6,6,6,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
#array_mot = [109]

#for i in range(109):
#    array_mot.append((zs[i]*30))

#plt.scatter(xs,ys,s=array_mot,c='red', alpha=0.4)
#plt.show()
#plt.savefig('motvestcasocit.pdf')
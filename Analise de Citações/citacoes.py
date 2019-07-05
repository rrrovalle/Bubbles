# libraries
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
from scipy import *

# definindo os dados de publico alvo, metodologias e qtd de citações

#array para manipular o z
array = [109]

#igual tabela (sem somatorio)
x = ('M','F','F','S','F','G','M','G','F','G','M/T/S','M','G','M/T','G','G','M','S','S','G','S','S','S','M','S','F/M','G','F','N/D','G','G','M','M','G','S','G','F/M','G','F','S','F','F/M','S','G','F/M','M','M','F/M','G','F','M','F','G','G','M/T','M/F/S','M','G','F','M','S','G','M','G','F','G','G','G','G','F','M','F','F','M','M','F/M','G','G','F/M','M','S','F','S','S','S','F/M','G','G','F/S','F','F','M','G','G','G','S','G','G','F','G','G','M','F/M','M/T','F','M/F/S','F/M','P','F')
y = ('N/D','DT','CT/DT','CT','CT','LB','CT/DT','LB','CT','C','CT','N/D','CT','CT','CT','RL','CT','CT','PS','C','CT/DT','CT','CT','CT','CT','CT/DT','CT','CT','CT/DT','C','CT','C','LB','LB','C','C','CT','LB','CT','ABP','C','CT','CT/DT','CT','PC','PC','CT','C','CT','CT','CT','RF','CT','CT','ABP','CT','C/DT','PC','N/D','PC','ABP','LB','CT/DT','LB','CT','CT/DT','PC','PC','PC','CT','N/D','CT','CT','CT','CT','CT','CT','CT','CT','CT','DD','LB','CT/DT','CT','N/D','CT','LB','LB','LB','CT','CT','MC','CT','LB','LB','CT','LB','LB','C','LB','CT','PS','ID','CT','CT','CT','C','CT','CT')
z = (51,49,43,43,30,21,19,17,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,9,9,9,8,8,8,8,7,7,6,6,6,6,6,6,6,6,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)

#preenchendo o array multiplicando para regular o tamanho da bolha
for i in range(109):
  array.append((z[i]*8))
  text(x[i], y[i], array[i], size=11, horizontalalignment='center')



plt.scatter(x,y,s=array,c='red',alpha=0.5)
plt.show()









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
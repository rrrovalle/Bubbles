import numpy as np
import matplotlib.pyplot as plt

N = 18
#Metodologias
CT = (0,0,1,1,4,5,9,11,12,23,27,36,44,54,74,92,101,110)
LB = (0,0,1,1,1,1,1,3,3,7,7,8,12,19,24,27,30,36)
C = (1,1,1,1,1,1,2,2,3,9,9,10,10,13,13,18,20,21)
DT = (0,0,0,0,0,0,0,0,0,1,4,8,8,12,15,15,15,15)
PC = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,9)
ND = (0,0,0,1,1,1,1,1,2,2,3,3,4,4,4,6,7,7)
ABP = (0,0,0,0,0,0,0,0,0,0,0,0,0,2,5,6,7,7)
PS = (3)

ind = np.arange(N)    # the x locations for the groups
width = 0.6  # the width of the bars

#Definir padrões
plt.plot(CT, marker='*', linestyle='-', color='#000000', label='Construtivista (CT)')
plt.plot(LB, marker='D', linestyle='-', color='#2F4F4F', label='Experimental (LB)')
plt.plot(C, marker='d', linestyle='-', color='#363636', label='Construcionista(C)')
plt.plot(DT, marker='H', linestyle='-', color='#00008B', label='Demonstrativo (DT)')
plt.plot(PC, marker='p', linestyle='-', color='#008B8B', label='Pensamento Computacional (PC)')
plt.plot(ABP, marker='P', linestyle='-', color='#6495ED', label='Abordagem Baseada em Problemas (ABP)')
plt.plot(ND, marker='h', linestyle='-', color='#00FFFF', label='N/D')


plt.legend()

plt.xticks(ind, ('2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012', '2013', '2014', '2015', '2016', '2017','2018'))
#plt.yscale('log')

plt.xticks(rotation=90)
#plt.xlabel('Anos analisados', fontsize=16)
plt.ylabel('Frequência Acumulada', fontsize=14)

#plt.show()
plt.savefig('teorias.pdf')
#plt.close()

#grafico aparentemente ok

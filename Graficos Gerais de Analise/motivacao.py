import numpy as np
import matplotlib.pyplot as plt

N = 18
#Motivation or Problem
CKR = (0,0,1,1,1,1,4,5,6,7,7,8,13,13,14,16,16,18)
DE = (1,1,1,1,1,1,2,2,2,5,5,6,7,10,13,19,23,29)
DEXP = (0,1,1,2,5,6,7,10,12,20,22,27,35,51,69,85,98,102)
EC = (0,0,0,0,0,0,0,0,0,1,1,1,1,3,4,4,4,5)
ER = (0,0,1,1,1,1,1,1,1,8,12,20,20,23,31,40,42,55)
RL = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4)

ind = np.arange(N)    # the x locations for the groups
width = 0.6  # the width of the bars

#Definir padrões
plt.plot(DEXP, marker='*', linestyle='-', color='#000000', label='Descrever Experiência/Metodologia (DEXP)  ')
plt.plot(ER, marker='D', linestyle='-', color='#2F4F4F', label='Estimular o Pensamento Lógico (ER)')
plt.plot(DE, marker='d', linestyle='-', color='#363636', label='Desenvolvimento de Software Educacional(DE)')
plt.plot(CKR, marker='H', linestyle='-', color='#00008B', label='Elaboração de um KIT de Robótica (CKR)')
plt.plot(EC, marker='p', linestyle='-', color='#008B8B', label='Estimular Interesse por Competições (EC)')
plt.plot(RL, marker='P', linestyle='-', color='#6495ED', label='Revisão de Literatura (RL)')

plt.legend()
plt.xticks(ind, ('2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012', '2013', '2014', '2015', '2016', '2017','2018'))

#plt.yscale('log')
plt.xticks(rotation=90)
#plt.xlabel('Anos analisados', fontsize=16)
plt.ylabel('Frequência Acumulada', fontsize=14)


#plt.show()
plt.savefig('motivacao.pdf')
#plt.close()

#grafico aparentemente ok

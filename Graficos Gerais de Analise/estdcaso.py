import numpy as np
import matplotlib.pyplot as plt

N = 18
#Case Study
AR = (0,1,3,3,4,4,6,7,7,13,15,19,25,30,42,64,74,89)
#CR = (0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2)
DS = (1,1,1,2,3,3,5,7,9,14,15,15,17,23,27,30,37,42)
EXP =(0,0,0,0,0,0,1,2,3,6,8,13,17,22,31,37,42,47)
#LB = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1)
RE = (0,0,0,0,1,2,2,2,2,8,9,13,15,20,25,25,26,27)
#RL = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1)
TC = (0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,4,4,4)

ind = np.arange(N)    # the x locations for the groups
width = 0.6  # the width of the bars

#Definir padrões
plt.plot(AR, marker='*', linestyle='-', color='#000000', label='Aula de Robótica (AR)')
#plt.plot(CR, marker='+', linestyle='-', color='#000080', label='CR')
plt.plot(DS, marker='D', linestyle='-', color='#2F4F4F', label='Desenvolvimento de Software (DS)')
plt.plot(EXP, marker='d', linestyle='-', color='#363636', label='Estudo Experimental/Pesquisa (EXP)')
#plt.plot(LB, marker='*', linestyle='-', color='#8B4513', label='LB')
plt.plot(RE, marker='H', linestyle='-', color='#00008B', label='Robótica Inserida na Sala de Aula (RE)')
#plt.plot(RL, marker='8', linestyle='-', color='#4B0082', label='RL')
plt.plot(TC, marker='p', linestyle='-', color='#008B8B', label='Treinamento para Competições (TC)')

plt.legend()

plt.xticks(ind, ('2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012', '2013', '2014', '2015', '2016','2017','2018'))
#plt.yscale('log')

plt.xticks(rotation=90)
#plt.xlabel('Anos analisados', fontsize=16)
plt.ylabel('Frequência Acumulada', fontsize=14)

#plt.show()
plt.savefig('estcaso.pdf')
#plt.close()

#grafico aparentemente o

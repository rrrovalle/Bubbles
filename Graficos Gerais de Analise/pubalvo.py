import numpy as np
import matplotlib.pyplot as plt

N = 18
#Target Public
F = (0,0,1,1,2,2,4,6,6,14,15,23,25,30,35,46,58,67)
G = (1,1,1,2,3,3,4,5,7,14,14,15,23,29,42,47,54,63)
M = (0,0,1,1,1,1,3,4,5,12,14,21,23,29,40,58,61,70)
ND = (0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1)
P = (0,0,0,0,0,0,0,0,0,1,1,1,1,2,2,2,2,3)
S = (0,1,1,1,1,2,3,4,4,6,10,15,19,26,30,31,32,33)
T = (0,0,0,0,0,0,1,2,2,2,2,5,5,6,7,8,9,10)


ind = np.arange(N)    # the x locations for the groups
width = 0.6  # the width of the bars

#Definir padrões
plt.plot(M, marker='*', linestyle='-', color='#000000', label='Ensino Médio (M)')
plt.plot(F, marker='D', linestyle='-', color='#2F4F4F', label='Ensino Fundamental (F)')
plt.plot(G, marker='d', linestyle='-', color='#363636', label='Geral (G)')
plt.plot(S, marker='H', linestyle='-', color='#00008B', label='Ensino Superior (S)')
plt.plot(T, marker='p', linestyle='-', color='#008B8B', label='Ensino Técnico (T)')
plt.plot(P, marker='P', linestyle='-', color='#6495ED', label='Primário (P)')
plt.plot(ND, marker='h', linestyle='-', color='#00FFFF', label='N/D')


plt.legend()

plt.xticks(ind, ('2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012', '2013', '2014', '2015', '2016', '2017','2018'))
#plt.yscale('log')

plt.xticks(rotation=90)
#plt.xlabel('Anos analisados', fontsize=16)
plt.ylabel('Frequência Acumulada', fontsize=14)

#plt.show()
plt.savefig('pbalvo.pdf')
plt.close()

#grafico aparentemente ok

import numpy as np
import matplotlib.pyplot as plt

N = 18
#Tools
AI = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,3,5)
ARD = (0,0,0,0,0,0,0,0,0,0,1,4,8,12,17,28,33,41)
MLB = (0,0,0,0,0,0,0,0,0,0,0,0,1,1,4,4,4,5)
MS = (0,0,0,0,1,2,2,3,4,12,14,19,20,24,37,47,54,60)
ND = (0,0,2,3,3,3,4,6,6,10,10,11,13,21,26,30,34,36)
OCV = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,4)
SC = (0,0,0,0,0,0,0,0,0,0,0,1,3,5,6,8,14,16)

ind = np.arange(N)    # the x locations for the groups
width = 0.6  # the width of the bars

#Patterns
plt.plot(MS, marker='*', linestyle='-', color='#000000', label='Mindstorms')
plt.plot(ARD, marker='D', linestyle='-', color='#2F4F4F', label='Arduino IDE')
plt.plot(ND, marker='d', linestyle='-', color='#363636', label='Nenhuma')
plt.plot(SC, marker='H', linestyle='-', color='#00008B', label='Scratch')
plt.plot(AI, marker='p', linestyle='-', color='#008B8B', label='App Inventor')
#plt.plot(OCV, marker='x', linestyle='-', color='#D2691E', label='Open-CV')

#plt.plot(ND, marker='.', linestyle='-', color='black', label='N/D')

plt.legend()

#fig.suptitle('test title', fontsize=20)
#plt.xlabel('Frequência', fontsize=16)
plt.ylabel('Frequência Acumulada', fontsize=14)

plt.xticks(ind, ('2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012', '2013', '2014', '2015', '2016','2017','2018'))
#plt.yscale('log')
plt.xticks(rotation=90)
#plt.show()
plt.savefig('ferramentas.pdf')
#plt.close()

#grafico aparentemente ok

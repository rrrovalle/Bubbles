import numpy as np
import matplotlib.pyplot as plt

N = 18
#Competitions
CBR = (0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2,2)
#CORA = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1)
FLL = (0,0,0,0,0,0,0,0,0,0,0,1,1,1,2,2,2,2)
#LARC = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1)
#ND = (1,2,4,5,8,9,14,18,21,40,46,57,71,91,115,143,166,188)
#OBI = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1)
OBR = (0,0,0,0,0,0,0,0,0,1,1,5,5,9,14,17,17,18)
RC = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1)
RBOMB = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,2)

ind = np.arange(N)    # the x locations for the groups
width = 0.6  # the width of the bars

#Definir padrões
plt.plot(OBR, marker='.', linestyle='-', color='#000000', label='Olimpíada Brasileira de Robótica (OBR)')
plt.plot(FLL, marker='+', linestyle='-', color='#000080', label='First Lego League (FLL)')
#plt.plot(RBOMB, marker='s', linestyle='-', color='#00FFFF', label='RBOMB - ')
plt.plot(CBR, marker='o', linestyle='-', color='#006400', label='Competição Brasileira de Robótica (CBR)')
plt.plot(RC, marker='*', linestyle='-', color='#8B4513', label='RoboCup (RC)')
#plt.plot(OBI, marker='x', linestyle='-', color='#D2691E', label='P')
#plt.plot(LARC, marker='.', linestyle='-', color='#4B0082', label='ND')
#plt.plot(CORA, marker='.', linestyle='-', color='black', label='CORA')
#plt.plot(ND, marker='x', linestyle='-', color='black', label='Nenhuma           ')
plt.legend()

plt.xticks(ind, ('2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012', '2013', '2014', '2015', '2016','2017','2018'))
#plt.yscale('log')
plt.xticks(rotation=90);

#plt.show()
plt.savefig('pbalvo.pdf')
plt.close()

#grafico aparentemente ok

import numpy as np
import matplotlib.pyplot as plt

N = 18

#Citações para gráfico doidão
#Zero = (10,4,5,5,9,21,8)
#Um = (1,6,2,2,3,1,0)

#Citação gráfico cumulativo

#todas as arquiteturas gerais
Arduino = (0,0,0,0,0,0,0,0,0,0,0,4,8,13,19,31,38,51)#ok
EV3 = (0,0,0,0,0,0,0,0,0,5,6,6,6,7,12,15,17,18)#ok
GoGoBoard = (0,0,0,0,0,0,0,1,2,2,2,2,2,2,2,2,2,2)#ok
Lego = (0,0,0,0,0,0,0,0,0,0,0,5,5,5,6,6,6,6)#ok
Micro_PIC = (0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2)#ok
Mindstorms = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,4,4)#ok
Nenhuma = (0,0,0,0,0,0,0,0,0,0,2,6,11,23,29,33,40,41)#ok
NXT = (0,0,0,0,0,0,0,0,1,7,13,14,15,16,20,24,29,32)#ok
Populu = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,2)#ok
Propria = (0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2)#ok
Raspberry_PI = (0,0,0,0,0,0,0,0,0,0,0,0,1,1,3,4,4,5)#ok
RCX = (1,2,2,2,3,4,4,4,4,5,5,5,5,5,5,5,5,5)
Scratch = (0,0,0,0,0,0,0,0,0,0,0,1,2,2,2,2,2,3)

ind = np.arange(N)    # the x locations for the groups
width = 0.6    # the width of the bars

#Definir padrões
plt.plot(Arduino,marker='*',linestyle='-',color='#000000',label='Arduino')
#plt.plot(Nenhuma,marker='D',linestyle='-',color='#2F4F4F',label='Nenhuma')
plt.plot(NXT,marker='d',linestyle='-',color='#2F4F4F',label='NXT')
plt.plot(EV3,marker='H',linestyle='-',color='#363636',label='EV3')
#plt.plot(Lego,marker='p',linestyle='-',color='#008B8B',label='Lego')
#plt.plot(RCX,marker='P',linestyle='-',color='#6495ED',label='RCX')
plt.plot(Raspberry_PI,marker='h',linestyle='-',color='#008B8B',label='Raspberry PI')
#plt.plot(Mindstorms,marker='>',linestyle='-',color='#006400',label='Mindstorms')
plt.plot(Propria,marker='<',linestyle='-',color='#6495ED',label='Propria')
#plt.plot(Scratch,marker='v',linestyle='-',color='#6B8E23',label='Scratch')
#plt.plot(GoGoBoard,marker='o',linestyle='-',color='#FF0000',label='GoGoBoard')
#plt.plot(Micro_PIC,marker='|',linestyle='-',color='#FF8247',label='Micro PIC')
#plt.plot(Populu,marker='.',linestyle='-',color='#EEEE00',label='Populu')


plt.legend()
plt.xticks(ind, ('2001','2002', '2003', '2004', '2005', '2006', '2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018'))
plt.xticks(rotation=90)

#plt.xlabel('Anos analisados', fontsize=16)
plt.ylabel('Frequência Acumulada', fontsize=14)

#plt.yscale('log')


#plt.show()
plt.savefig('arqalt.pdf')
#plt.close()
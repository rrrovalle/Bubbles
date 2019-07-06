import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#definindo o eixo x (anos)
X_AXIS = (
'   2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014',
'2015','2016','2017','2018'
)

#definindo o index(x,label)
index = pd.Index(X_AXIS, name='Anos Analisados')

#definindo o dataset dos eventos
data = {
        'WRE': (0,0,0,0,0,0,0,0,0,12,0,10,9,12,19,23,0,8),
        'SBIE': (1,1,0,1,0,1,4,2,2,2,1,0,0,6,4,7,10,9),
        'WEI': (0,0,0,0,0,0,0,0,0,0,4,4,2,4,4,2,3,4),
        'WIE': (0,0,2,0,3,0,1,2,1,5,1,1,3,2,4,1,10,5)
}

#montando
df = pd.DataFrame(data, index=index)

ax = df.plot(kind='bar', stacked=True, figsize=(15, 10), fontsize=15)
ax.set_ylabel('Quantidade de Publicações', fontsize=15)

bars = ax.patches
patterns =('-', '+', 'x','/','//','O','o','\\','\\\\')
hatches = [p for p in patterns for i in range(len(df))]
for bar, hatch in zip(bars, hatches):
    bar.set_hatch(hatch)

ax.legend(loc=4, bbox_to_anchor=(1, 1), ncol=4, fontsize=15)

#print
plt.savefig('qtdartigosporevento.pdf')
#plt.show()
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\Rodrigo Valle\Desktop\sbie.csv')
df = pd.DataFrame(data, columns=['Teoria','Publico','Citacoes'])

x = []
y = []
z = []

#eu mudei para str/int mas n sei, pq mesmo assim n funcionou
for i in df:
    x.append(df['Teoria'].astype(str))
    y.append(df['Publico'].astype(str))
    z.append(df['Citacoes'].astype(int))
#aqui eu iria chamar o text() e pegar o nome ou valor da posição desejada

#plotting
plt.scatter(x, y, s=z, alpha=0.5)
plt.show()
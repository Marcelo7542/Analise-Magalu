import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings

warnings.filterwarnings("ignore")

BaseDados = pd.read_excel("Vase_004 - Magalu - Sem Resolução.xlsx")

Data = BaseDados.set_index("Data")

MediaM = Data['Fechamento'].rolling(5).mean()
MediaT = Data['Fechamento'].rolling(30).mean()




BaseDados['Mes'] = BaseDados['Data'].dt.month
plt.figure(figsize=(16,5))
plt.title("Análise de Dados das ações da Magalu", fontsize=16)
sns.boxplot(data=BaseDados, x="Mes", y="Fechamento")

print(BaseDados.groupby(['Mes']).describe()['Fechamento'])

plt.show()




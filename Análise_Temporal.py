
import pandas as pd

import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")

BaseDados = pd.read_excel("Vase_004 - Magalu - Sem Resolução.xlsx")


# print(BaseDados.head())
# print(BaseDados.info())
# print(BaseDados.shape)
# print(BaseDados.describe())

Data = BaseDados.set_index("Data")

MediaM = Data['Fechamento'].rolling(5).mean()
MediaT = Data['Fechamento'].rolling(30).mean()

plt.style.use("grayscale")
plt.figure(figsize=(17,5))
plt.title("Análise de Dados das ações da Magalu", fontsize=16)

plt.plot(Data.index, Data['Fechamento'], color="Blue")
plt.plot(Data.index, MediaM, color="Red")
plt.plot(Data.index, MediaT, color="Green")
plt.xlabel("Período", fontsize=10)
plt.ylabel("Valor da Ação", fontsize=10)
plt.legend(labels=["Fechamento", "Média Móvel (5 dias)", "Média Móvel (20 dias)"])
plt.show()

# Dados.tail()
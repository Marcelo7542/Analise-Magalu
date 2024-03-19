
import pandas as pd
import plotly.graph_objects as go

import warnings

warnings.filterwarnings("ignore")

BaseDados = pd.read_excel("Vase_004 - Magalu - Sem Resolução.xlsx")


Dados = BaseDados.set_index("Data")

Grafico = go.Figure(
    data=[
          go.Candlestick(
              x= Dados.index,
              open = Dados['Abertura'],
              high = Dados['Maior'],
              low = Dados['Menor'],
              close = Dados['Fechamento'],
          )
    ]
)

Grafico.update_layout( xaxis_rangeslider_visible=False )

Grafico.show()
import pandas as pd

df = pd.read_excel("NATU3_evolucao.xlsx")
print(df)
df["valor"]
df["valor"].max()
df["valor"].min()
df["valor"].mean()
df["valor"].std()
df[0:5]
df[0:1]["valor"]
colunas = ["conta", "valor"]
df[23:24][colunas]
linhas = df["trimestre"] == "20262T"
colunas = ["conta", "valor"]
df[linhas][colunas]
linhas= df["conta"] == "lucro"
colunas = ["valor"]
df[linhas][colunas].mean()

import seaborn as sns
import matplotlib.pyplot as plt
linhas = df["conta"] == "lucro"
colunas = ["trimestre", "valor"]
sns.lineplot(dados, x= "trimestre", y= "valor")
plt. title("gráfico de lucro")
plt. xticks(rotation=45)

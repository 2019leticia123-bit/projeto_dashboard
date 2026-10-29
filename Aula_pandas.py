import pandas as pd

df = pd.read_csv("alunos_Desempenho.csv")
df.head()
df.columns
colunas=["aluno","curso","periodo"]
df[colunas]

pd.read_excel("alunos_localidade_carro_merge.xlsx")
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
df = pd.read_excel("NATU3_evolucao.xlsx")
linhas = df["conta"] == "lucro"
colunas = ["trimestre", "valor"]
dados = df[linhas][colunas]
fig, ax= plt.subplots()
sns.lineplot(dados, x= "trimestre", y= "valor")

tab1, tab2 = st.tabs(["Tab 1","Tab 2"])
with tab1:
    st.pyplot(fig)
    st.title("Dashboard da Natura")
    st.pyplot(fig)
    st.dataframe(df)

with tab2:
    df = pd.read_excel("planilhao_b3.xlsx")
    st.dataframe(df)
    df_size = df.groupby("setor").size()
    fig, ax = plt.subplots()
    sns.barplot(df_size)
    ax.set_title("Grafico do numero de empresas por setor")
    st.pyplot(fig)


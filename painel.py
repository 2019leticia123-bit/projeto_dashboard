import pandas as pd
import plotly.express as px
import streamlit as st

# 1. Configuração da página para o modo Wide (tela cheia elegante)
st.set_page_config(
    page_title="Corporate Dashboard | Natura &Co",
    page_icon="🌿",
    layout="wide",
)

# 2. Cabeçalho Institucional (Logo + Informações)
# URL de um logo público e transparente da Natura para o topo
LOGO_URL = "https://seeklogo.com"

col_logo, col_titulo = st.columns([1, 4])

with col_logo:
  st.image(LOGO_URL, width=150)

with col_titulo:
  st.title("Natura &Co (B3: NATU3)")
  st.subheader("Painel de Desempenho Corporativo e Análise Setorial")

# Breve descrição informativa sobre o momento da empresa
st.markdown("""
    **Sobre a Natura &Co:** Líder global no setor de cosméticos e beleza, a Natura foca em inovação sustentável e canais de relacionamento multicanal. 
    A empresa concluiu recentemente sua simplificação corporativa focando fortemente na expansão estrutural da América Latina.
    """)
st.write("---")

# 3. Bloco de Métricas de Destaque rápidos (KPIs)
col_kpi1, col_kpi2, col_kpi3 = st.columns(3)
with col_kpi1:
  st.metric(label="Ticker Principal", value="NATU3 / NTCO3", delta="B3 Novo Mercado")
with col_kpi2:
  st.metric(label="Foco Geográfico", value="América Latina", delta="Consolidado")
with col_kpi3:
  st.metric(label="Lucratividade Recorrente", value="Margem 14.6%", delta="Full Year")

st.write("")

# 4. Criação das Abas Separadas por Escopo
tab1, tab2 = st.tabs([
    "📈 Evolução de Resultados (Natura)",
    "📊 Análise de Mercado (Setores B3)",
])

# --- ABA 1: EVOLUÇÃO NATURA ---
with tab1:
  st.markdown("### Histórico Financeiro e de Evolução")

  try:
    df_natu = pd.read_excel("NATU3_evolucao.xlsx")

    # Tratamento e filtro dos dados informados por você
    linhas = df_natu["conta"].str.lower() == "lucro"
    dados_filtrados = df_natu[linhas]

    if not dados_filtrados.empty:
      # Criando gráfico interativo de linha refinado com a paleta institucional (Laranja/Natura)
      fig1 = px.line(
          dados_filtrados,
          x="trimestre",
          y="valor",
          title="Evolução do Lucro por Trimestre",
          markers=True,
          color_discrete_sequence=["#D2691E"],  # Tom terracota/laranja institucional
          labels={"trimestre": "Trimestre", "valor": "Valor (R$)"},
      )

      # Estilizando o layout interno do gráfico para ficar limpo
      fig1.update_layout(
          plot_bgcolor="rgba(0,0,0,0)",
          xaxis=dict(showgrid=True, gridcolor="LightGrey"),
          yaxis=dict(showgrid=True, gridcolor="LightGrey"),
      )

      st.plotly_chart(fig1, use_container_width=True)
    else:
      st.warning(
          "Nenhum dado encontrado para o filtro de conta 'lucro' na planilha."
      )

    # DataFrame em um container expansível para não poluir o visual principal
    with st.expander("Visualizar dados brutos (Tabela)"):
      st.dataframe(df_natu, use_container_width=True)

  except Exception as e:
    st.error(f"Erro ao carregar o arquivo 'NATU3_evolucao.xlsx': {e}")


# --- ABA 2: ANÁLISE SETORIAL B3 ---
with tab2:
  st.markdown("### Distribuição de Empresas Listadas por Setor")

  try:
    df_b3 = pd.read_excel("planilhao_b3.xlsx")

    # Contabilizando o tamanho por setor
    df_size = (
        df_b3.groupby("setor")
        .size()
        .reset_index(name="Quantidade")
        .sort_values(by="Quantidade", ascending=False)
    )

    # Gráfico de barras interativo ordenado e moderno (Paleta degradê discreta)
    fig2 = px.bar(
        df_size,
        x="setor",
        y="Quantidade",
        title="Número de Empresas Listadas por Setor de Atuação",
        color="Quantidade",
        color_continuous_scale="Oranges",  # Transição elegante de tons laranja
        labels={"setor": "Setor de Atuação", "Quantidade": "Nº de Empresas"},
    )

    fig2.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_tickangle=-45,
        showlegend=False,
    )

    st.plotly_chart(fig2, use_container_width=True)

    with st.expander("Visualizar planilha consolidada da B3"):
      st.dataframe(df_b3, use_container_width=True)

  except Exception as e:
    st.error(f"Erro ao carregar o arquivo 'planilhao_b3.xlsx': {e}")



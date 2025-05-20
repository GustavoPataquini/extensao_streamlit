import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Gráfico de Barras por Aba do Excel")

# Função para carregar as abas do Excel
@st.cache_data
def carregar_abas(arquivo):
    return pd.read_excel(arquivo, sheet_name=None, engine='openpyxl')

# Upload do arquivo
arquivo_excel = st.file_uploader("Faça upload de um arquivo Excel (.xlsx)", type=["xlsx"])

if arquivo_excel:
    abas = carregar_abas(arquivo_excel)  # dicionário com {nome_aba: DataFrame}
    
    # Seleciona a aba
    aba_escolhida = st.selectbox("Escolha a aba para visualizar", list(abas.keys()))
    df = abas[aba_escolhida]

    st.subheader(f"Dados da aba: {aba_escolhida}")
    st.dataframe(df)

    # Seleciona colunas para o gráfico de barras
    colunas_categoricas = df.select_dtypes(include=['object', 'category']).columns
    colunas_numericas = df.select_dtypes(include=['number']).columns

    if not colunas_categoricas.empty and not colunas_numericas.empty:
        eixo_x = st.selectbox("Selecione a coluna categórica (X)", colunas_categoricas)
        eixo_y = st.selectbox("Selecione a coluna numérica (Y)", colunas_numericas)

        # Gráfico de barras com Seaborn
        st.subheader("Gráfico de Barras")
        fig, ax = plt.subplots()
        sns.barplot(data=df, x=eixo_x, y=eixo_y, ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)
    else:
        st.warning("A aba selecionada precisa ter pelo menos uma coluna categórica e uma numérica.")




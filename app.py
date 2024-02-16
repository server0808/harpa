import streamlit as st
import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import math

st.sidebar.title('Ferramentas')
st.sidebar.markdown('---')
st.sidebar.subheader('Calculadora Black-Scholes-Merton')

#st.image('/home/vinicio/Dropbox/Fortem/GitHub/harpa/harpa2.jpg', width=250)
st.title('Harpa Quant')
st.text('Estudos quantitativos para auxiliar a tomada de decisão de investidores.')
st.markdown("[Comunidade no Discord](https://discord.gg/MaF7wZDQvZ)")
st.markdown('---')

# Função para calcular o preço da opção Black-Scholes-Merton
def black_scholes_call_put(S, K, T, r, sigma, option_type):
    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    
    if option_type == 'call':
        option_price = S * norm_cdf(d1) - K * math.exp(-r * T) * norm_cdf(d2)
    elif option_type == 'put':
        option_price = K * math.exp(-r * T) * norm_cdf(-d2) - S * norm_cdf(-d1)
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")
    
    return option_price

# Função de distribuição cumulativa normal padrão (CDF)
def norm_cdf(x):
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0

# Título do aplicativo
st.subheader('Calculadora Black-Scholes-Merton')

# Organizando os campos de entrada em duas colunas
col1, col2 = st.columns(2)

# Entrada dos valores dos parâmetros
with col1:
    S = st.number_input('S - preço spot do ativo', min_value=0.0)
    K = st.number_input('K - preço de exercício da opção', min_value=0.0)
    T = st.number_input('T - vencimento da opção, como fração do ano', min_value=0.0)
with col2:
    r = st.number_input('r - taxa de juros anual, como fração', min_value=0.0)
    sigma = st.number_input('Sigma - volatilidade, como fração', min_value=0.0)
    option_type = st.selectbox('Tipo de opção', ['call', 'put'])

# Botão para calcular o preço da opção
if st.button('Calcular preço da opção'):
    option_price = black_scholes_call_put(S, K, T, r, sigma, option_type)
    st.write(f'O preço da {option_type} é: ${round(option_price,2)}')
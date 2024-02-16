import streamlit as st
import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

st.sidebar.title('Ferramentas')
st.sidebar.markdown('---')

st.image('/home/vinicio/Dropbox/Fortem/GitHub/harpa/harpa2.jpg', width=250)
st.title('Harpa Quant')
st.text('Estudos quantitativos para auxiliar a tomada de decisão de investidores.')
st.markdown('---')

st.markdown("[Comunidade no Discord](https://discord.gg/MaF7wZDQvZ)")

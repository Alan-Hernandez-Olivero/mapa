import streamlit as st
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/Alan-Hernandez-Olivero/mapa/main/data.csv')
st.write(df)
st.map(df)

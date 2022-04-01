import streamlit as st
import pandas as pd

df = pd.read_csv('https://raw.github.com/Alan-Hernandez-Olivero/mapa/blob/main/data.csv')
st.write(df)
st.map(df)

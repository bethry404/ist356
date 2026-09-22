import streamlit as st
import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv"
df = pd.read_csv(url)

st.dataframe(df)


col1 = [1, 2, 3, 4]
col2 = [3, 2, 4, 1]
same = set(col1) == set(col2)

st.write(f"Are the columns the same? {same}")
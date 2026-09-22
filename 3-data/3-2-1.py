import streamlit as st
import pandas as pd
import numpy as np

# does it have a header
# is it first row header == an number
# what is the row delimiter == \n
# what is the cell/field delimiter == \s

url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/delimited/webtraffic.log"

data = pd.read_csv(url, delimiter=' ', skiprows=3, ) # <---

st.title("Web Traffic Data")

filter = (data['sc-status'] == 200) & (data['time-taken'] > 500)
dataNew = data[filter]

st.dataframe(dataNew)
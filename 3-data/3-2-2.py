import streamlit as st
import pandas as pd
import numpy as np
import requests

response = requests.get("https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/json-samples/employees.json")
json_data = response.json()


output = pd.json_normalize(json_data, record_path="employees", meta=["dept"])

st.title("Employee Data")
st.dataframe(output)
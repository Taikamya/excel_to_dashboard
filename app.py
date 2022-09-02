from local_settings import EXCEL

import pandas as pd
# import plotly.express as px
# import streamlit as st

with open(EXCEL, "rb") as f:
    data = f.read()

df = pd.read_excel(
    io=data,
    engine='openpyxl',
    sheet_name='Sales',
    skiprows=3,
    usecols='B:R',
    nrows=1100,
)
df.index += 1

dframe = pd.DataFrame(df)

print(dframe)

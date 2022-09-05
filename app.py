from local_settings import EXCEL

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Sample Dashboard",
                   page_icon=":bar_chart:")


with open(EXCEL, "rb") as f:
    data = f.read()

df = pd.read_excel(
    io=data,
    engine='openpyxl',
    sheet_name='Sample',
    skiprows=3,
    usecols='B:R',
    nrows=1100,
)   # type:ignore
df.index += 1

dframe = pd.DataFrame(df)

print(dframe)

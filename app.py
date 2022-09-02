from local_settings import EXCEL

import pandas as pd
# import plotly.express as px
# import streamlit as st

df = pd.read_excel(
    io=EXCEL,
    engine='openpyxl',
    sheet_name='Sales',
    skiprows=3,
    usecols='B:R',
    nrows=1000,
)


print(df)

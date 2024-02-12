import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from st_pages import add_page_title
# from streamlit_apex_charts import line_chart, bar_chart, pie_chart, area_chart, radar_chart

add_page_title()

st.write("This is just a dashboard page!")

#Gathering data
df_data_customers = pd.read_csv('customers_dataset.csv')

#Cek apa ada data duplikat
df_data_customers_duplicate = df_data_customers.duplicated().values.any()
print('ada data duplikat di data customers = ', df_data_customers_duplicate)

#customers_dataset
df_data_negara = df_data_customers['customer_state'].value_counts()

tab1, tab2 = st.tabs(["Table", "Diagram Batang"])

with tab1:
    st.header("Tabel")

with tab2:
    st.header("BAR CHART")

    chart_data = pd.DataFrame(df_data_negara.values, columns=["a"], index=df_data_negara.index)
    
    st.bar_chart(chart_data)

    st.pyplot(fig)





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
    st.header("Table")


with tab2:
    st.header("BAR CHART")
    # Plot diagram batang
    # df_data_negara.plot()
    chart_data = pd.DataFrame(df_data_negara.values, columns=["a"], index=df_data_negara.index)
    # st.dataframe(df_data_negara)
    st.bar_chart(chart_data)

    # line_chart('Line chart',chart_data)
    # c1, c2 = st.columns(2)
    # with c1:
	#     bar_chart('Bar chart',chart_data)
	#     pie_chart('Pie chart',chart_data)
    # with c2:
	#     area_chart('Area chart',chart_data)
	#     radar_chart('Radar chart',chart_data)
          
        #Pengiriman Tepat Waktu dan Terlambat
    data_keterlambatan = pd.DataFrame(
        'Kategori': ['Tepat Waktu', 'keterlambatan'],
        'Jumlah': [111,222]
    })
        
    st.dataframe(data_keterlambatan)

    #Grafik Keterlambatan
    label = data_keterlambatan['Kategori'] 
    size = data_keterlambatan['Jumlah']

    fig, ax = plt.subplots()
    ax.pie(size, labels=label, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Mengatur aspek rasio agar lingkaran tampak sempurna

    st.pyplot(fig)





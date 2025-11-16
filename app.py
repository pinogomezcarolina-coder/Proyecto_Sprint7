import streamlit as st
import pandas as pd
import plotly.express as px

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Crear un encabezado
st.header('Análisis de Datos de Vehículos')

# Botón para histograma
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para la columna "odometer"')
    
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón para scatter plot
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión: odometer vs price')
    
    fig2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)


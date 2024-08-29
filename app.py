import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Análisis de datos de vehículos')
car_data = pd.read_csv('vehicles_us.csv')  # leer los datos


# Casilla de verificación para el histograma
build_histogram = st.checkbox('Construir un histograma')
if build_histogram:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Casilla de verificación para el gráfico de dispersión
build_scatter_plot = st.checkbox('Mostrar gráfico de dispersión')
if build_scatter_plot:
    st.write(
        'Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

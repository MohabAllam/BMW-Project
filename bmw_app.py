
import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

st.image('bmw.jpg')
df = pd.read_csv('bmw.csv')
st.title('EDA of used BMW cars')
st.write('# Year of production VS Price')

st.selectbox('Select Model Type', df.model.unique())
st.sidebar.slider('Select Year of Production', 1996, 2020)
st.sidebar.slider('Car Price', 1200.0, 123456.0)
st.radio('Transmission Type', df.transmission.unique())
st.sidebar.slider('Mileage', 1.0, 214000.0)
st.selectbox('Fuel Type', df.fuelType.unique())

chart = st.selectbox('Select plot type', ['Histogram', 'Boxplot'])

if chart == "Histogram":
    st.plotly_chart(px.histogram(df, 'year'))

else:
    st.plotly_chart(px.box(df, 'year'))

# Numerical Features
st.write('# Numerical features')
num_cols = df.select_dtypes(exclude= 'object').columns
for col in num_cols:
    fig = px.histogram(df, col)
    st.plotly_chart(fig)

# Cat Features
cat_cols = df.select_dtypes(include= 'object').columns
st.write('# Categorical features')
for col in cat_cols:
    fig = px.histogram(df, col)
    st.plotly_chart(fig)

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 12:56:47 2022

@author: barim
"""

import streamlit as st
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px


data = pd.read_csv('nycairbnb.csv')

featureset = ['RoomType', 'neighbourhood', 'longitude', 'latitude', 'bedrooms', 'price', 'instant_bookable']
graphset = ["Histogram", "Box Plot", "Enhanced Box Plot", "Strip Plot", "Violin Plot", "Swarm Plot"]


st.title('Customer dashboard')

#Show the raw data
st.subheader('Raw data')
st.write(data)

#Let the user choose graph, features, etc.
st.subheader('Visualization')
col1, col2 = st.columns(2)
with col1: 
    st.subheader('Choices')
    title = st.text_input('Enter a title for the chart')
    kind1 = st.selectbox('Pick plot for left side', graphset, key="pl")
    x = st.selectbox("Feature for x:", featureset, key="f1l")
    if kind1 != "Histogram":
        y = st.selectbox("Feature for y:", featureset, key="f2l")
        hue = st.selectbox("Feature for hue:", (featureset), key="h2l")
    if kind1 == "Histogram": 
        kde = st.selectbox("Do you want to add a kde?", (True, False), key="k1")
        color1 = st.color_picker('Pick a color for Plot 1', key="c1")
#Then view the graph
with col2:
    fig = plt.figure(figsize=(7, 5))
    if kind1 == "Histogram": sns.histplot(data = data, x = x, kde = kde, color = color1)
    if kind1 == "Box Plot": sns.boxplot(data = data, x = x, y = y, hue = hue)
    if kind1 == "Enhanced Box Plot": sns.boxenplot(data = data, x = x, y = y, hue = hue)
    if kind1 == "Strip Plot": sns.stripplot(data = data, x = x, y = y, hue = hue)  
    if kind1 == "Violin Plot": sns.violinplot(data = data, x = x, y = y, hue = hue)
    if kind1 == "Swarm Plot": sns.swarmplot(data = data, x = x, y = y, hue = hue)
#User can input a title for the graph
    plt.title(title)
    st.pyplot(fig)
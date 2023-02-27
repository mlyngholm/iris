import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Page Configuration
st.set_page_config(page_title='Prediction app',
                   layout='wide',
                   initial_sidebar_state='expanded')


# Title of the app
st.title('Simple Prediction App')

# Load Dataset
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/iris.csv')

st.write(df)

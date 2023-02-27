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


# Input Widgets
st.sidebar.subheader('Input features')
sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.8)
sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.1)
petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 3.8)
petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 1.2)

# Separate X and y
X = df.drop(columns='Species')
y = df.Species

# Data splitting
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model building
model = RandomForestClassifier(max_depth=2, max_features=4, n_estimators=200, random_state=42)

model.fit(X_train, y_train)


# Apply model to make predictions
y_pred = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])


# Print EDA
st.subheader('Brief EDA')
st.write('The data is grouped by the class and the variable mean is computed for each class')
groupby_species_mean = df.groupby('Species').mean()

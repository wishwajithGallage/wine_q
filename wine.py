# -*- coding: utf-8 -*-


import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

wine_model = pickle.load(open('wine1_model.sav', 'rb'))





# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Wine_Quality_Prediction',
                          
                          ['Wine_Quality_Prediction'],
                          icons=['activity'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Wine_Quality_Prediction'):
    
    # page title
    st.title('Wine_Quality_Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        fixed_acidity= st.text_input('fixed_acidity')
        
    with col2:
        volatile_acidity = st.text_input('volatile_acidity')
    
    with col3:
       citric_acid = st.text_input('citric_acid')
    
    with col1:
       residual_sugar = st.text_input('residual_sugar')
    
    with col2:
       chlorides= st.text_input('chlorides')
    
    with col3:
        free_sulfur_dioxide = st.text_input('free_sulfur_dioxide')
    
    with col1:
        total_sulfur_dioxide = st.text_input('total_sulfur_dioxide')
    
    with col2:
        density = st.text_input('density')
        
    with col3:
        pH = st.text_input('pH')
        
    with col1:
        sulphates = st.text_input('sulphates')
        
    with col2:
        alcohol = st.text_input('alcohol')    
        
        
    
    
    # code for Prediction
    Wine_Quality_ = ''
    
    # creating a button for Prediction
    
    if st.button('wine Test Result'):
        Wine_Quality_Prediction = wine_model.predict([fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol])
        
        if (Wine_Quality_Prediction[0] == 1):
          Wine_Quality_ = 'Good Quality Wine'
        else:
          Wine_Quality_ = 'Bad Quality Wine'
        
    st.success(Wine_Quality_)





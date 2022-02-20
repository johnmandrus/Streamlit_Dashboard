#------------------------------------------------------------------------------------#
#IMPORTS                                                                             |
#------------------------------------------------------------------------------------#
import streamlit as st
#------------------------------------------------------------------------------------#



#------------------------------------------------------------------------------------#
#CREATE STREAMLIT DASHBOARD                                                          |
#------------------------------------------------------------------------------------#

sidebar = st.sidebar.radio("Navigation",["Home","EDA","Turbofan Dashboard","About Us"])

if sidebar == "Home":
    header = st.container()
    with header:
        st.title('PeraML')
        st.header('Failure Prediction for Rotating Machinery')
    
    with open('homepage.txt', 'r') as file:
        home_text = file.read()

    project_description = st.container()
    with project_description:
        st.text(home_text)

if sidebar == "EDA":
    header = st.container()
    with header:
        st.title('Exploratory Data Analysis')

if sidebar == "Turbofan Dashboard":
    header = st.container()
    with header:
        st.title('Dashboard Goes Here')

if sidebar == "About Us":
    john, harvi, omar = st.columns(3)

    with john:
        st.image("john.jpg",caption="John Andrus",use_column_width=True)
    
    with harvi:
        st.image("harvi.jpg",caption="Harvi Singh",use_column_width=True)

    with omar:
        st.image("omar.jpg",caption="Omar Kapur",use_column_width=True)
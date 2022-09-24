import streamlit as st
from PIL import Image
import pandas as pd



def About_diamond():

    st.title("Sentimental Analysis : ")
    image = Image.open('images/intro.png')
    st.image(image, caption='Introduction')
    image = Image.open('images/intro2.png')
    st.image(image, caption='Introduction')
    df_data=pd.read_csv("Data/projectData.csv")
    df_data_vac=pd.read_csv('Data/projectData_vac_data1.csv')
    df_vaccines=pd.read_csv('Data/projectData_vaccines.csv')
    tweet_df = pd.read_csv('Data/projectData_twitter_data1.csv')


    agree = st.checkbox('Display Data')

    if agree:
        st.write("Here's our Complete information about  data")

        st.write(df_data)

    agree = st.checkbox('Display vac Data')

    if agree:
        st.write("Here's our Complete information about vac data")

        st.write(df_data_vac)
    agree = st.checkbox('Display twitter Data')

    if agree:
        st.write("Here's our Complete information about twitter data")

        st.write(tweet_df)
    agree = st.checkbox('Display all vaccinations related data')

    if agree:
        st.write("Here's our Complete information about vaccinations")

        st.write(df_vaccines)
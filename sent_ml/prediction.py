import streamlit as st
import numpy as np
from pickle import load
import pandas as pd

import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

df_data=pd.read_csv("Data/projectData.csv")
df_data_vac=pd.read_csv('Data/projectData_vac_data1.csv')
df_vaccines=pd.read_csv('Data/projectData_vaccines.csv')

tweet_df = pd.read_csv('Data/projectData_twitter_data1.csv')

vectorizer=load(open('Models/vect.pkl','rb'))
model=load(open('Models/logistic.pkl','rb'))

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()



def show_predict_page():



    y = tweet_df.pop('sentiment')
    x = tweet_df

    from imblearn.under_sampling import RandomUnderSampler

    rus = RandomUnderSampler(random_state=42, replacement=True)# fit predictor and target variable
    x_rus, y_rus = rus.fit_resample(x, y)

    tweet_df['sentiment']=y_rus
    tweet_df.dropna(inplace=True)

    original_title = '<p style="font-family:cursive; color:white; font-size: 60px;">Sentimental Analysis</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    #st.title("Diamond Price Prediction")
    original_title1 = '<p style="font-family:cursive; color:white; font-size: 30px;">We need some tweet </p>'
    st.markdown(original_title1, unsafe_allow_html=True)
    tweet=st.text_area('Text to analyze','tweet')
    btn_click=st.button("Positive/Negative")
    if btn_click==True:
        if tweet:
            def preprocess_test(raw_tweet):
                    # Remove Special Character
                letters_only = re.sub('[^a-zA-Z]',' ',raw_tweet)
    
                # Conver sentence into Lower Case
                letters_only = letters_only.lower()
    
                 # Tokenize
                words = letters_only.split()
    
                #Remove Stop Words
                words = [w for w in words if not w in stopwords.words('english')]
    
                 # Stemming
    
                words = [stemmer.stem(word) for word in words]
    
                clean_tweet = ' '.join(words)
    
                return clean_tweet

           
    
               
    
            clean_tweet = preprocess_test(tweet)
    
            clean_tweet_vector = vectorizer.transform([clean_tweet])
    
            prediction = model.predict(clean_tweet_vector)

            if prediction == 0:
                pred='Negative Sentiment'
                st.snow()
            else:
                 pred='Positive Sentiment'
                 st.balloons()

            
    
            st.success(pred)
            st.snow()
            

        else:
            st.error("Enter the correct values")

            
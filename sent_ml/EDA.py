import streamlit as st
from PIL import Image
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS
#import create_wordcloud

def show_explore_page():
    df_data=pd.read_csv("Data/projectData.csv")
    df_data_vac=pd.read_csv('Data/projectData_vac_data1.csv')
    df_vaccines=pd.read_csv('Data/projectData_vaccines.csv')
    tweet_df = pd.read_csv('Data/projectData_twitter_data1.csv')

    df = tweet_df.loc[tweet_df['sentiment'] == 'Negative',:]
    words = ' '.join(df['Text'])
    cleaned_words = ' '.join([word for word in words.split()
                            if 'http' not in word
                              and not word.startswith('@')
                                and word != 'RT'
                            ])
    wordcloud = WordCloud(stopwords = STOPWORDS,
                     background_color = 'black',
                     height = 1500,
                     width = 1500).generate(cleaned_words)
    
    
    st.title("wordcloud for positive tweets: ")
    image = Image.open('images/pos.png')
    st.image(image, caption='wordcloud')
    st.title("wordcloud for negative tweets: ")
    image = Image.open('images/neg.png')
    st.image(image, caption='wordcloud')
    st.title("wordcloud for neutral tweets: ")
    image = Image.open('images/neutral.png')
    st.image(image, caption='wordcloud')
  

   
    st.title("Correlation map")
    fig = plt.figure(figsize=(10, 4))
    sns.heatmap(df_data_vac[['New_doses_oneday','total_doses','fully_vaccinated']].corr(), annot=True)
    st.pyplot(fig)

    s_c=df_data_vac[['location','percentage']]
    vac_df_pop=s_c.copy()
    vac_df_pop['percentage'] = vac_df_pop['percentage'].apply(lambda x:float(x.strip('%')))
    vac_df_pop['percentage']=vac_df_pop['percentage'].astype(int)
    vac_df_pop1=vac_df_pop[:5].copy()
    vac_df_pop1
    st.title("Top 5 fully vaccinated countries")
    fig = plt.figure(figsize=(10, 4))
    sns.barplot(x='location',y='percentage',data=vac_df_pop1)
    st.pyplot(fig)
    st.title("Top 40 fully vaccinated countries")
    fig = plt.figure(figsize=(10, 4))
    sns.barplot(x='location',y='percentage',data=vac_df_pop.nlargest(40, 'percentage'))
    st.pyplot(fig)
   
    

   






import streamlit as st
import numpy as np
from pickle import load
import pandas as pd

from About import About_diamond
#from EDA import show_explore_page
import base64
from prediction import show_predict_page
from About import About_diamond
from EDA import show_explore_page
page=st.sidebar.selectbox("Explore or predict or About",{"predict","Explore","About"})

if(page=="predict"):

       

    show_predict_page()
elif(page=="Explore"):
    show_explore_page()

else:
    
    About_diamond()
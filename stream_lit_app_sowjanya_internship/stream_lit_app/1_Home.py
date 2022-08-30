import streamlit as st
import pandas as pd

import numpy as np
st.set_page_config(
    page_title="Multipage App"
    
)

st.title("Main Page")
st.sidebar.success("Select a page above")

data_frame=pd.read_csv("pubs.csv")

agree = st.checkbox('Display Data')

if agree:
     st.write("Here's our Complete information about publocation data")

     st.write(data_frame)

st.map(data_frame)

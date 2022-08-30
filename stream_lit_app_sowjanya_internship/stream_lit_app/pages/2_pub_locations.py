import streamlit as st
import pandas as pd
st.title("Pub Locations based on ZIP Code/Local Authority")
data_frame=pd.read_csv("pubs.csv")
option = st.multiselect(
    'Enter either postalcode/local_authority to find the pub locations : ',
    ['postalcode', 'local_authority'])

if 'postalcode' in option: 
    postalcode1 = st.text_input('Enter the postalcode to find the locations : ')
    if postalcode1: 
        st.write(f'The pub locations for the {postalcode1} are !')
        
        rslt_df = data_frame[data_frame['postcode'] == postalcode1]
        st.map(rslt_df)
elif 'local_authority' in option:
    local_authority1 = st.text_input('Enter the local authority to find the locations : ')
    if local_authority1:
        st.write(f'The pub locations for the {local_authority1} are!')
        rslt_df = data_frame[data_frame['local_authority'] == local_authority1]
        st.map(rslt_df)




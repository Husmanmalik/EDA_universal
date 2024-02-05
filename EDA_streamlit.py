import streamlit as st 
import pandas as pd 
import numpy as np 
import seaborn as sns 
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# webapp title
st.markdown('''
# **Exploratory Data Analysis web application**
''')
# how to upload file from pc

with st.sidebar.header("Upload your Dataset(.csv)"):
    uploaded_file = st.sidebar.file_uploader("Upload your file",type=['csv'])
    df=pd.read_csv('titanic.csv')
# profiling report for pandas
if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv=pd.read_csv(uploaded_file)
        return csv
    df=load_csv()
    pr=ProfileReport(df,explorative=True)
    # display the profile report in sidebar
    st.header('**Input DataFrame**')
    st.write(df)
    st.header('**Profiling report with pandas**')
    st_profile_report(pr)
else:
    st.info("Awaiting for CSV file,")# bhai kuch upload to kar do
    if st.button('Press to use example Data'):
      #example dataset
       @st.cache
       def load_data():
           df=sns.load_dataset('titanic')
           pr =ProfileReport(df,explorative=True)
           st.header('**Input Dataframe**')
           st.write('---')
           st.header('**Pandas Profiling Report**')
           st_profile_report(df)
           
    


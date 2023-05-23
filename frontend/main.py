import requests
import streamlit as st
from io import StringIO
import pandas as pd

# Title of my app
st.title("PancNet app")


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

   requests.post(dataframe.to_json(orient='columns'))
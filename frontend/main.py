import requests
import streamlit as st
from io import StringIO
import pandas as pd
import json

# Title of my app
st.title("PancNet app")


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:

    # Can be used wherever a "file-like" object is accepted:
    df = pd.read_csv(uploaded_file)
    st.write(df)

    assert set(df.columns) == set(['age', 'code', 'date'])

    d = {
        "age": df.age.tolist(), 
        "code": df.code.tolist(), 
        "date": df.date.tolist()
    }

    print (f"requesting {json.dumps(d)}")
    
    # IMPORTANT the address below works with the docker compose only
    # it should be change to localhost if one wants to interactively run frontend and backend
    response = requests.post("http://backend:8080/predict", json.dumps(d)) 
    print (response.text)
import streamlit   as st
import pandas as pd
import pickle
import numpy as np
st.title('App de deteccion de fraudes')
from PIL import Image
image = Image.open('delsur.png')
st.image(image, caption='Delsur')



uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)






# Load  the model from disk

if st.button("Predict"):
    pickle_in = open('modelinicial.pkl', 'rb')
    model = pickle.load(pickle_in)
    predict=model.predict(test)
  

    st.text(f"""
     The number of items in the day is :  {predict} 
    """)    # Get the input features
    # run predictions





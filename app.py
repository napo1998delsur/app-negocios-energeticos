import streamlit   as st
st.title('Negocios Energeticos App')
from PIL import Image
image = Image.open('delsur.png')
st.image(image, caption='Delsur')

import streamlit as st
import pandas as pd
import pickle
import numpy as np

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)


st.subtitle('Upload file to predict')
# features for prediction 
# X = sales_join[['day', 'month', 'id','spree_store_id','total_sales']]
#y = sales_join['items_total']

# Add a heading for input features
st.subheader('Enter  Features for Predictions')


test=pd.read_csv('model')

# Load  the model from disk

if st.button("Predict"):
    pickle_in = open('finalized_model.pkl', 'rb')
    model = pickle.load(pickle_in)
    predict=model.predict(test)
  

    st.text(f"""
     The number of items in the day is :  {predict} 
    """)    # Get the input features
    # run predictions


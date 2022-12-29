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
    predict_2=model.predict(dataframe)

predict_2=model.predict(dataframe)
pred_df = pd.DataFrame(predict_2,columns=["Prediccion"])
pred_df.to_csv('salidadatos.csv', header=True, index_label='Id')
st.write(pred_df)


@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(pred_df)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='predicccion.csv',
    mime='text/csv',
)




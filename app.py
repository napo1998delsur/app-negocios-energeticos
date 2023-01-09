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
    pickle_in = open(r'C:\Users\nperez\Documents\GitHub\app-negocios-energeticos\modelinicial.pkl', 'rb')
    model = pickle.load(pickle_in)
    y=model.predict([[dataframe]])
    pred_df = pd.DataFrame(y,columns=["Prediccion"])
    pred_df.to_csv('salida.csv', header=True, index_label='N°')
    prediccion={0:'Fraude',
            1:'No Fraude',     }
    pred_df['Tipo_prediccion']=pred_df['Prediccion'].map(prediccion)
    pred_df.to_csv('salida.csv', header=True, index_label='N°')
    pred_df.head()
    st.write(pred_df)
    
   
    # Different ways to use the API
output=pd.read_csv('salida.csv')
print(output['Prediccion'].unique())
prediccion={0:'Fraude',
            1:'No Fraude',      
            }
output['Tipo_prediccion']=output['Prediccion'].map(prediccion)
    # end def
join=pd.merge(dataframe,output, how='outer', on='N°')
st.write(join)
reporte=join.to_excel('reporte.csv')
@st.experimental_memo
def convert_df(join):
   return join.to_csv(index=False).encode('utf-8')


csv = convert_df(join)

st.download_button(
   "Press to Download",
   csv,
   "reporte.csv",
   "text/csv",
   key='download-csv'
)










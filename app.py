import streamlit   as st

st.title('Negocios Energeticos App')

from PIL import Image
image = Image.open('delsur.png')

st.image(image, caption='Delsur')



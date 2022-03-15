import streamlit as st
from PIL import Image
import numpy as np

st.file_uploader("Upload an image", type=["jpg", "png"])

uploaded_file=st.file_uploader("ファイルアップロード", type='png')
image=Image.open(uploaded_file)
img_array = np.array(image)
st.image(img_array,caption = 'サムネイル画像',use_column_width = True)
import streamlit as st
from PIL import Image
import numpy as np

st.file_uploader("Upload an image", type=["jpg", "png"])

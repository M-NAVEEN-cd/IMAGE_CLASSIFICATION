
import streamlit as st
import numpy as np
from skimage.io import imread
from skimage.transform import resize
import pickle
from PIL import Image
st.title("Image Classifier")
st.text("upload the image")

model = pickle.load(open('img_model.p','rb'))
uploadede_file = st.file_uploader("Choose an image. . . .",type="jpg")
if uploaded_file is not None:
 img = Image.open(uploaded_file)
 st.image(img,caption='Uploaded image')

 if st.button('PREDICT'):
  Categories = ['CAT','DOG','FISH']
  st.write('Result. . .')
  flat_data = []
 img = np.array(img)
 img_resized = resize(img,(150,150,3))
 flat_data.append(img_resized.flatten())
 flat_data=np.array(flat_data)
 print(img.shape)
 plt.imshow(img_resized)
 y_out = model.predict(flat_data)
 y_out =Categories[y_out[0]]
 print(f' PREDICTION BY THE MODEL : {y_out}')

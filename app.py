import streamlit as st
import tensorflow as tf
from keras.models import load_model
from PIL import Image
import numpy as np

# Load your custom model
model = load_model('resnet50v2.h5')

# Define a function to preprocess the image and make predictions
def predict(image):
    # Resize the image to the input size expected by the model
    image = image.resize((224, 224))  # Modify the size according to your model's expected input
    # Convert the image to a numpy array
    image_array = np.array(image)
    # Normalize the image array (optional, depending on your model's training)
    image_array = image_array / 255.0
    # Expand dimensions to match the input shape of the model
    image_array = np.expand_dims(image_array, axis=0)
    # Make prediction
    prediction = model.predict(image_array)
    return prediction

# Streamlit app layout
st.title('Custom Model Image Prediction App')

# Get user input
st.header('Upload an Image')
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    # When the user clicks the 'Predict' button
    if st.button('Predict'):
        try:
            # Make prediction
            prediction = predict(image)
            # Display the prediction
            st.header('Prediction')
            st.write(prediction)
        except Exception as e:
            st.error(f"Error: {e}")


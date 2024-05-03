import cv2
import numpy as np
import streamlit as st
import tensorflow as tf

# Load the trained model from the HDF5 file
model = tf.keras.models.load_model("sign_language_model.h5")

# Function to predict sign language for numbers using the model
def predict_sign(image):
    image = cv2.resize(image, (64, 64))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = np.expand_dims(image, axis=0) / 255.0
    prediction = model.predict(image)
    return np.argmax(prediction), np.max(prediction) * 100

# Streamlit UI
st.title("Sign Language for Numbers")
st.write("Click the start checkbox to open webcam and capture sign language for numbers.")

# CSS to inject contained in a triple-quoted string.
css_style = """
<style>
    .predict-text { color: #4CAF50; font-size: 20px; }
    .frame-box { border: 2px solid #FFC107; }
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)

# Start capturing webcam
run = st.checkbox("Start")

if run:
    camera = cv2.VideoCapture(0)
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            prediction_text = st.empty()  # Placeholder for displaying prediction text
        with col2:
            latest_frame = st.empty()  # Placeholder for displaying the latest frame

    while run:
        ret, frame = camera.read()
        if not ret:
            break

        # Predict the sign language for numbers
        sign, accuracy = predict_sign(frame)

        # Display the predicted number and accuracy text
        prediction_text.markdown(f"<div class='predict-text'>Predicted Number: {sign}   Accuracy: {accuracy:.2f}%</div>", unsafe_allow_html=True)

        # Display the frame
        latest_frame.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), channels="BGR", caption="Live Webcam Feed", use_column_width=True)

    camera.release()
    cv2.destroyAllWindows()

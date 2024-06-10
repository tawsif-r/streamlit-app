# Skin Lesion Classification Application

## Overview

This application leverages machine learning to predict the class of a skin lesion from an image. The model classifies lesions into one of seven categories:

1. Melanocytic nevi
2. Melanoma
3. Benign keratosis-like lesions
4. Basal cell carcinoma
5. Actinic keratoses
6. Vascular lesions
7. Dermatofibroma

## Features

- **Image Upload**: Upload an image of a skin lesion.
- **Prediction**: The model predicts the lesion class.
- **Probability Scores**: View the probability scores for each of the seven classes.
- **User-Friendly Interface**: Easy-to-use interface for both clinicians and patients.

## Prerequisites

- Python 3.7 or higher
- TensorFlow 2.x
- streamlit
- OpenCV (for image processing)
- NumPy
- Pandas

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/tawsif-r/streamlit-app.git
    cd streamlit-app
    ```

3. Install the required packages:
    ```bash
    pip install streamlit
    ```

4. Download the pre-trained model and place it in the `model` directory.

## Usage

1. Start the streamlit web server:
    ```bash
    streamlit run app.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000`.

3. Upload an image of the skin lesion.

4. View the predicted class and probability scores.
   ![alt text](https://github.com/tawsif-r/streamlit-app/blob/main/home.png?raw=true)


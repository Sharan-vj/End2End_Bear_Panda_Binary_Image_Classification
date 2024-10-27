# Import Dependencies
import io
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from pathlib import Path
from tensorflow.keras.models import load_model  # type: ignore
from tensorflow.keras.preprocessing.image import load_img, img_to_array  # type: ignore


# Image Predictor Class
class ImagePredictor:
    def __init__(self, model_path: Path, model_weights: Path | None, 
                 img_size: tuple, class_names: list):
        
        # Load the base model from the specified path
        self.model = load_model(model_path)

        # If weights are provided, load them into the model
        if model_weights:
            self.model.load_weights(model_weights)
            print(f"Model weights loaded from: {model_weights}")

        self.img_size = img_size
        self.class_names = class_names

    def predict_image(self, image_path):
        try:
            # Load and preprocess the image
            img = load_img(image_path, target_size=self.img_size)
            img_array = img_to_array(img) / 255.0
            img_array = np.expand_dims(img_array, axis=0)

            # Make a prediction
            prediction = self.model.predict(img_array)
            pred_index = np.argmax(prediction)
            predicted_class = self.class_names[pred_index]
            confidence = np.max(prediction)

            return predicted_class, confidence

        except FileNotFoundError:
            print(f"Error: The file '{image_path}' was not found.")
            return "", 0.0  # Return default values on error
        except Exception as e:
            print(f"An error occurred: {e}")
            return "", 0.0  # Return default values on error


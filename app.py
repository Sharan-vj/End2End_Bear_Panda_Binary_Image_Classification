# Import Dependencies
from io import BytesIO
from pathlib import Path
from flask import Flask, jsonify, request, render_template
from binaryClassifier.utils.predictors import ImagePredictor


# Initialize Flask App
app = Flask(__name__)


# Model Configurations
class_names = ["Bear", "Panda"]
predictor = ImagePredictor(
            model_path=Path('models/base_model.h5'),
            model_weights=Path('models/model.weights.h5'),
            img_size=(256, 256),
            class_names=class_names
        )


# Default route
@app.route("/")
def home():
    return render_template("index.html")


# Prediction route
@app.route('/predict', methods=['POST'])
def prediction():
    if request.method == 'POST':
        file = request.files['file']
        try:
            # Read the image file and make prediction
            image_file = BytesIO(file.read())
            pred, conf = predictor.predict_image(image_path=image_file)
            
            # Print the prediction for debugging purposes    
            print(f"Prediction Class: {pred}")
            print(f"Confidence Score: {conf}")

            # Return the prediction as a JSON response
            return jsonify({"Predicted Class": pred})
        except Exception as e:
            raise e


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=False)
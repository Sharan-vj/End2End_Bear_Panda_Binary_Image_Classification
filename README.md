# End2End Bear-Panda Binary Image Classification Using Transfer Learning

### Project Description
<p align='justify'>This project presents a complete end-to-end machine learning workflow to classify images of bears and pandas using a fine-tuned **VGG19** model. With the goal of accurately distinguishing between these two animals, the model leverages transfer learning to enhance prediction performance. A web-based application is built to allow users to upload images and instantly receive classification results.</p>

### Screenshots
<img width="800" height="400" align="center" src="/screenshots/sample_image.png">

### Technologies Used in This Project
* Python: For model development and backend integration
* TensorFlow/Keras: For implementing and fine-tuning the VGG19 model
* Pandas & NumPy: For data processing and manipulation
* Flask: For deploying the model as a web application
* Jupyter Notebook: For Exploratory Data Analysis (EDA) and model development
* HTML/CSS: For designing the web-based user interface
* Git/GitHub: For version control and project collaboration
* Docker: For containerizing the application
* GitHub Actions: To automate CI/CD workflows
* AWS: For hosting and deployment of the web app

### Model Performance
<img width="800" height="400" align="center" src="/screenshots/accuracy.png">

### Installation and Setup

1. **Clone the Repository**:
    ```bash
    git clone End2End_Bear_Panda_Binary_Image_Classification.git
    cd End2End_Bear_Panda_Binary_Image_Classification
    ```

2. **Create a Virtual Environment**:
    ```bash
    conda create --name <env name> python=3.10 -y
    ```
3. **Activate the Virtual Enviroment**
    ```bash
    conda activate <env name>
    ```
4. **Install the Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Run the Flask Application**:
    ```bash
    python app.py
    ```
    The application will be available at `http://127.0.0.1:8080/`.


### Usage
* Upload Image: Use the web interface to upload an image of a bear or panda.
* Get Prediction: The fine-tuned `VGG19` model will classify the image as either a bear or a panda, displaying the result instantly.

### Dataset
* The dataset used in this project contains labeled images of bears and pandas. The data is stored in the data/ directory. The model is trained on a balanced dataset to ensure consistent performance across both classes.

### Model
* **Model Architecture**: VGG19
* **Fine-tuning**: The final few layers of the VGG19 model were re-trained on the bear vs. panda dataset to enhance accuracy.
* **Model Saving**: The base model is saved as `base_model.h5` and The model trained weights are saved as `model.weights.h5` inside the models/ directory for easy reuse.

### Contributing
* Contributions are welcome! If you have any suggestions or improvements, please raise an issue or submit a pull request.

### License
* This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

### Acknowledgments
* Special thanks to the open-source community for the libraries used in this project.
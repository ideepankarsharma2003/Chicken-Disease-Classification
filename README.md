# **`Chicken Disease Classification using Fecal Images`**

![Project Image](OIP.jpg)

## Overview

The "Chicken Disease Classification using Fecal Images" project is a comprehensive solution aimed at detecting and classifying diseases in chickens by analyzing fecal images. Leveraging machine learning techniques and web technology, this project provides an efficient and automated approach to disease management in poultry farming.


## Workflows

1. Update config.yaml
2. Update secrets.yaml [optional]
3. Update params.yaml 
4. Update the entity
5. Update the configuration manager in src/config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml <!-- MLops tool to keep track of the CI/CD pipeline -->



## Features

- **Web Application**: The project includes a Flask-based web application that allows users to interact with the disease classification system.
- **DVC Pipelining**: Deep Version Control (DVC) pipelining is employed to organize and manage the various stages of data preprocessing, model training, and evaluation.
- **Data Ingestion**: Fecal images are ingested into the system, serving as the basis for disease classification.
- **Base Model Preparation**: The project prepares a base model architecture for further customization and training.
- **Model Training**: The base model is fine-tuned using the fecal image dataset to achieve accurate disease classification.
- **Model Evaluation**: The trained model is evaluated using a test dataset to measure its classification performance.
- **User-Friendly Interface**: The web application offers a user-friendly interface for uploading images and receiving disease classification results.

## Prerequisites

- Python 3.x
- Flask
- TensorFlow
- DVC

## Setup and Usage

1. Clone the repository.
2. Install the required Python packages using `pip install -r requirements.txt`.
3. Start the Flask web application: `python app.py`.
4. Access the web application through a web browser by visiting `http://localhost:8080`.

## Project Structure

- `app.py`: Main Flask application file.
- `config.yaml`: Configuration file containing various parameters.
- `src/ChickenDiseaseClassifier/`: Main project directory.
  - `pipeline/`: DVC pipeline stages.
    - `stage_01_dataingestion.py`: Data ingestion stage.
    - `stage_02_prepare_base_model.py`: Prepare the base model stage.
    - `stage_03_training.py`: Model training stage.
    - `stage_04_model_evaluation.py`: Model evaluation stage.
  - `components/`: Additional project components.
    - `prepare_callbacks.py`: Custom callbacks for model training.
  - `utils/`: Utility functions and scripts.
    - `common.py`: Common functions for image processing.
  - `static/`: Static files for the Flask web application.
  - `templates/`: HTML templates for the web application.

## Contact

For inquiries, feel free to contact [Deepankar Sharma](https://github.com/ideepankarsharma2003/) at [deepankarsharma2003@gmail.com](deepankarsharma2003@gmail.com).

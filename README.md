# Wine Quality Prediction - MLOps Project

This is an End-to-End Machine Learning project that predicts the quality of wine based on various physicochemical properties. The project implements a complete ML pipeline including data ingestion, validation, transformation, model training, and evaluation, and exposes the model via a Flask web application.

## Table of Contents
- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Pipeline Stages](#pipeline-stages)
- [License](#license)

## Project Overview
The goal of this project is to predict wine quality using a machine learning model. It utilizes a modular pipeline approach to ensure reproducibility and maintainability. Experiment tracking is handled by MLflow.

## Project Structure
```
MLOPS_Project/
├── app.py                  # Flask application entry point
├── main.py                 # Main script to run the ML training pipeline
├── params.yaml             # Configuration parameters for the pipeline
├── requirements.txt        # Project dependencies
├── setup.py                # Package setup script
├── config/                 # Configuration files
├── research/               # Notebooks for experimentation
├── src/                    # Source code
│   └── ML_PROJECT/
│       ├── components/     # Logic for each pipeline stage
│       ├── config/         # Configuration management
│       ├── constants/      # Project constants
│       ├── entity/         # Data classes for configuration
│       ├── pipeline/       # Pipeline orchestration
│       └── utils/          # Utility functions
├── static/                 # Static assets for the web app
├── templates/              # HTML templates
└── winequality-data...     # Dataset
```

## Technologies Used
- **Programming Language:** Python
- **Web Frmework:** Flask
- **Machine Learning:** Scikit-learn, Pandas, NumPy
- **Experiment Tracking:** MLflow
- **Configuration Management:** YAML, Box

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd MLOPS_Project
    ```

2.  **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the Web Application
To start the Flask web application for prediction:

```bash
python app.py
```
Open your browser and navigate to `http://localhost:8080`.

### Running the Training Pipeline
To execute the complete training pipeline (Ingestion -> Validation -> Transformation -> Training -> Evaluation):

```bash
python main.py
```

## Pipeline Stages
The training pipeline consists of the following stages:
1.  **Data Ingestion:** Downloads and extracts the dataset.
2.  **Data Validation:** Validates the data schema and types.
3.  **Data Transformation:** Preprocesses the data for training.
4.  **Model Trainer:** Trains the model (ElasticNet).
5.  **Model Evaluation:** Evaluates the model and logs metrics to MLflow.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

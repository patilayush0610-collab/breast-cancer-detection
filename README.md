# breast-cancer-detection
A machine learning-powered web application for early breast cancer detection that predicts whether a tumor is benign or malignant based on medical diagnostic features.
# Breast Cancer Detection Web App

## Overview
Breast Cancer Detection is a Machine Learning-based web application that helps predict whether a breast tumor is Benign (non-cancerous) or Malignant (cancerous) using diagnostic medical data. The application provides quick and accurate predictions through an easy-to-use web interface.

## Features
- Predicts breast cancer diagnosis
- User-friendly web interface
- Machine Learning-powered predictions
- Instant results
- Responsive design
- Easy deployment and usage

## Technologies Used
- Python
- Flask
- Machine Learning
- Scikit-learn
- Pandas
- NumPy
- HTML
- CSS

## Dataset
The model is trained using the Breast Cancer Wisconsin Diagnostic Dataset, which contains medical features extracted from digitized images of breast mass cell nuclei.

## Project Structure

```text
Breast_Cancer_Detection/
│
├── app.py
├── model.pkl
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── notebook.ipynb
└── README.md
```

## How It Works
1. Enter the required medical diagnostic values.
2. Click the Predict button.
3. The trained machine learning model processes the input data.
4. The application displays whether the tumor is Benign or Malignant.

## Machine Learning Workflow
- Data Collection
- Data Preprocessing
- Feature Selection
- Model Training
- Model Evaluation
- Web Application Deployment

## Future Enhancements
- Improved model accuracy
- Data visualization dashboard
- Patient report generation
- Cloud deployment
- Multi-model comparison

## Installation

```bash
pip install -r requirements.txt
python app.py
```

## Author
Ayush Patil

## License
This project is created for educational and portfolio purposes.

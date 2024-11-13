# Solar Energy Production Predictor

A Streamlit web application that predicts solar energy production based on ambient temperature and solar irradiance using machine learning models.

## Description

This application uses trained machine learning models to predict solar energy output. Users can input ambient temperature and solar irradiance values through an intuitive web interface to get instant predictions of energy production in watts.

## Features

- User-friendly web interface
- Support for multiple ML models
- Input validation and helpful tooltips

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository: git clone https://github.com/yourusername/solar-energy-predictor.git
cd solar-energy-predictor
2. Create and activate a virtual environment (optional but recommended):
Windows
python -m venv venv
venv\Scripts\activate
3. Install required packages:
pip install -r requirements.txt


solar-energy-predictor/
├── app.py
├── model_utils.py
├── models/
│ ├── scaler.pkl
│ ├── Linear Regression_model.pkl
│ └── Gradient Boosting Regressor_model.pkl
├── requirements.txt
└── README.md


## Running the Application

1. Ensure all models are present in the `models/` directory
2. Run the Streamlit application:
streamlit run app.py

3. Open your web browser and navigate to `http://localhost:8501` (or the URL provided in the terminal)

## Usage

1. Enter the ambient temperature (°C) in the first input field
2. Enter the solar irradiance (W/m²) in the second input field
3. Click "Generate Prediction" to get the predicted energy output

## Model Information

The application supports multiple machine learning models:
- Linear Regression
- Gradient Boosting Regressor

The models should be trained separately and saved in the `models/` directory with the naming convention `{model_name}_model.pkl`.

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

[Add your chosen license here]

## Authors

[Add your name and contact information here]

This README.md provides:
A clear description of the application
Installation instructions
Project structure
Dependencies
Running instructions
Usage guidelines
Model information
Sections for contributing, license, and authors
You should customize the following parts:
Repository URL
License information
Author information
Any specific requirements or additional features of your implementation
Remember to also create the requirements.txt file as specified in the README.
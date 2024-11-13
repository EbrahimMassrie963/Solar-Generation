# model_utils.py
import joblib
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import pickle

# Load the scaler
scaler = joblib.load('models/scaler.pkl')  # assuming you saved the scaler during training

def normalize_data(data, columns):
    """
    Normalize the specified columns using the loaded scaler.
    """
    # Reshape data for compatibility with older scikit-learn versions
    data_array = data[columns].values
    transformed_data = scaler.transform(data_array)
    data[columns] = transformed_data
    return data


def predict_energy(temp, radiation, selected_model="Gradient Boosting Regressor"):
    """
    Predict energy output using multiple models and return all predictions.
    """
    # List of available models
    models = {
        "Gradient Boosting Regressor": "Gradient Boosting Regressor_model.pkl",
        "Linear Regression": "Linear Regression_model.pkl"
    }
    
    # Create a DataFrame with the input values
    new_data = pd.DataFrame({
        'Amb_Temp': [temp],
        'radiation': [radiation],
    })
    
    # Normalize the input data
    input_features = ['Amb_Temp', 'radiation']
    # Reshape data for compatibility with older scikit-learn versions
    input_array = new_data[input_features].values
    new_data[input_features] = scaler.transform(input_array)
    
    # Get predictions from all models
    predictions = {'others': {}}
    
    for model_name, model_file in models.items():
        try:
            model = joblib.load(f'models/{model_file}')
            pred = model.predict(new_data[input_features])[0]
            
            if model_name == selected_model:
                predictions['selected'] = pred
            else:
                predictions['others'][model_name] = pred
        except FileNotFoundError:
            continue
    
    return predictions

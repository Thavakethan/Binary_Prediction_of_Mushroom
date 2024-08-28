import pandas as pd
import xgboost as xgb
from sklearn.preprocessing import LabelEncoder
import os

def preprocess_data(file_path):
    data = pd.read_csv(file_path)
    
    # Example preprocessing - adjust as needed
    # Assuming 'class' is the target column
    if 'class' in data.columns:
        y = data['class']
        X = data.drop(['class'], axis=1)
        
        # Example encoding
        encoder = LabelEncoder()
        for col in X.select_dtypes(include=['object']).columns:
            X[col] = encoder.fit_transform(X[col])
        
        return X, y
    else:
        raise ValueError("Data does not contain 'class' column")

def predict_mushrooms(file_path):
    X, _ = preprocess_data(file_path)
    
    # Load your trained model (adjust path if needed)
    model = xgb.XGBClassifier()
    model.load_model('backend/xgboost_model.json')
    
    # Predict
    predictions = model.predict(X)
    
    # Save results
    result_file = 'results/predictions.csv'
    results_df = pd.DataFrame(predictions, columns=['prediction'])
    results_df.to_csv(result_file, index=False)
    
    return result_file

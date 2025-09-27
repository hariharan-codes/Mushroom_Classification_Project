import os
import joblib
import pandas as pd

MODEL_FOLDER = "models"

# Load all models
models = {}
for filename in os.listdir(MODEL_FOLDER):
    if filename.endswith(".pkl"):
        model_name = filename.replace(".pkl", "")
        models[model_name] = joblib.load(os.path.join(MODEL_FOLDER, filename))

# Load processed columns and target mapping
processed_csv = "data/processed/mushrooms_processed.csv"
processed_df = pd.read_csv(processed_csv)
FEATURE_COLUMNS = [c for c in processed_df.columns if c != "class"]

# Mapping numeric back to 'e'/'p'
target_mapping = {0: 'e', 1: 'p'}

def predict(input_data: dict, model_name: str = "random_forest"):
    """
    Predict mushroom class using specified model.
    Returns 'e' for edible, 'p' for poisonous.
    """
    if model_name not in models:
        raise ValueError(f"Model '{model_name}' not found. Available models: {list(models.keys())}")
    
    df_input = pd.DataFrame([input_data])
    
    # Clean column names
    df_input.columns = [c.strip().replace("-", "_") for c in df_input.columns]
    
    # One-hot encode categorical features
    df_input = pd.get_dummies(df_input)
    
    # Find missing columns and add them all at once to avoid fragmentation warning
    missing_cols = [col for col in FEATURE_COLUMNS if col not in df_input.columns]
    if missing_cols:
        df_input = pd.concat([df_input, pd.DataFrame(0, index=df_input.index, columns=missing_cols)], axis=1)
    
    # Ensure column order matches training features
    df_input = df_input[FEATURE_COLUMNS]
    
    model = models[model_name]
    prediction_numeric = model.predict(df_input)[0]
    
    # Map numeric prediction back to 'e'/'p'
    prediction_label = target_mapping[prediction_numeric]
    
    return prediction_label

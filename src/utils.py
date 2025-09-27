import pandas as pd
import os
import joblib
from sklearn.preprocessing import LabelEncoder

RAW_DATA_PATH = "data/raw/mushrooms.csv"
PROCESSED_DATA_PATH = "data/processed/mushrooms_processed.csv"
FEATURE_ENCODER_PATH = "models/encoders/feature_columns.pkl"
TARGET_ENCODER_PATH = "models/encoders/target_encoder.pkl"

def load_data():
    """Load raw mushroom dataset."""
    if not os.path.exists(RAW_DATA_PATH):
        raise FileNotFoundError(f"Raw data not found at {RAW_DATA_PATH}")
    df = pd.read_csv(RAW_DATA_PATH)
    return df

def preprocess_data(df: pd.DataFrame, return_encoders=False):
    """
    Preprocess dataset:
    - Clean column names
    - Strip whitespace in string values
    - One-hot encode features
    - Encode target to numeric (0/1)
    - Save processed data and encoders
    """
    # Clean column names
    df.columns = [c.strip().replace("-", "_") for c in df.columns]

    # Strip whitespace in string values
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # Separate features and target
    X = df.drop("class", axis=1)
    y = df["class"]

    # One-hot encode categorical features
    X_encoded = pd.get_dummies(X)

    # Encode target labels numerically
    target_encoder = LabelEncoder()
    y_encoded = target_encoder.fit_transform(y)

    # Save processed data
    os.makedirs(os.path.dirname(PROCESSED_DATA_PATH), exist_ok=True)
    df_processed = pd.concat([X_encoded, pd.Series(y_encoded, name="class")], axis=1)
    df_processed.to_csv(PROCESSED_DATA_PATH, index=False)

    # Save feature columns
    os.makedirs(os.path.dirname(FEATURE_ENCODER_PATH), exist_ok=True)
    joblib.dump(X_encoded.columns.tolist(), FEATURE_ENCODER_PATH)

    # Save target encoder
    joblib.dump(target_encoder, TARGET_ENCODER_PATH)

    if return_encoders:
        return X_encoded, y_encoded, X_encoded.columns.tolist(), target_encoder
    else:
        return X_encoded, y_encoded

def eda(df: pd.DataFrame):
    """Perform basic EDA and print results."""
    print("\n=== Dataset Info ===")
    print(df.info())

    print("\n=== Summary Statistics ===")
    print(df.describe(include='all'))

    print("\n=== Missing Values ===")
    print(df.isnull().sum())

    print("\n=== Value Counts for Categorical Columns ===")
    for col in df.columns:
        if df[col].dtype == 'object':
            print(f"\n-- {col} --")
            print(df[col].value_counts())

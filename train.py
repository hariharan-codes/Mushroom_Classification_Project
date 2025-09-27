import os
import joblib
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from xgboost import XGBClassifier
import numpy as np

from src.utils import load_data, preprocess_data, eda

# ----------------------------
# Configuration
# ----------------------------
MODEL_FOLDER = "models"
EXPERIMENT_NAME = "Mushroom_Classification"
np.random.seed(42)

os.makedirs(MODEL_FOLDER, exist_ok=True)

# ----------------------------
# Load and preprocess data
# ----------------------------
df_raw = load_data()
X, y, feature_columns, target_encoder = preprocess_data(df_raw, return_encoders=True)

# Perform EDA
eda(df_raw)

# Train/test split (stratified)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ----------------------------
# Define models
# ----------------------------
models = {
    "random_forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "xgboost": XGBClassifier(n_estimators=100, use_label_encoder=False, eval_metric='mlogloss', random_state=42),
    "logistic_regression": LogisticRegression(max_iter=500, random_state=42),
    "decision_tree": DecisionTreeClassifier(random_state=42),
    "gradient_boosting": GradientBoostingClassifier(n_estimators=100, random_state=42),
    "svm": SVC(probability=True, random_state=42)
}

# ----------------------------
# Save feature columns and target encoder
# ----------------------------
ENCODER_FOLDER = os.path.join(MODEL_FOLDER, "encoders")
os.makedirs(ENCODER_FOLDER, exist_ok=True)
joblib.dump(feature_columns, os.path.join(ENCODER_FOLDER, "feature_columns.pkl"))
joblib.dump(target_encoder, os.path.join(ENCODER_FOLDER, "target_encoder.pkl"))

# ----------------------------
# MLflow experiment setup
# ----------------------------
mlflow.set_experiment(EXPERIMENT_NAME)

# ----------------------------
# Train, evaluate, save, log
# ----------------------------
for name, model in models.items():
    try:
        with mlflow.start_run(run_name=name):
            # Train
            model.fit(X_train, y_train)

            # Predict
            y_pred = model.predict(X_test)

            # Overall metrics
            acc = accuracy_score(y_test, y_pred)
            prec = precision_score(y_test, y_pred, average='macro')
            rec = recall_score(y_test, y_pred, average='macro')
            f1 = f1_score(y_test, y_pred, average='macro')

            # Print metrics
            print(f"\n=== Model: {name} ===")
            print(f"Accuracy : {acc:.4f}")
            print(f"Precision: {prec:.4f}")
            print(f"Recall   : {rec:.4f}")
            print(f"F1 Score : {f1:.4f}")

            # Save model
            model_path = os.path.join(MODEL_FOLDER, f"{name}.pkl")
            joblib.dump(model, model_path)
            print(f"✅ Model saved: {model_path}")

            # Log metrics to MLflow
            mlflow.sklearn.log_model(model, artifact_path="model")
            mlflow.log_metric("accuracy", acc)
            mlflow.log_metric("precision", prec)
            mlflow.log_metric("recall", rec)
            mlflow.log_metric("f1_score", f1)

    except Exception as e:
        print(f"❌ Training failed for {name}: {e}")
        continue

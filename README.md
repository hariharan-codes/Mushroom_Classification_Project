# 🍄 Mushroom Classification – ML Deployment Project

This project builds a **Mushroom Edible vs. Poisonous Classifier** using multiple machine learning models, tracks experiments with **MLflow**, and deploys the final application with a **FastAPI backend** and **Streamlit frontend** inside a **Dockerized environment** on **Render**.

---

## 🚀 Workflow

1. **Data Preprocessing & Feature Encoding**

   * Loaded the [Kaggle Mushroom Classification Dataset](https://www.kaggle.com/uciml/mushroom-classification).
   * Applied label encoding for categorical features.
   * Created training and test splits.

2. **Model Training**
   Trained and compared performance across 6 ML models:

   * Logistic Regression
   * Decision Tree
   * Random Forest
   * Gradient Boosting
   * XGBoost
   * SVM

3. **Experiment Tracking with MLflow**

   * Logged metrics, parameters, and artifacts for all models.
   * Compared experiments visually in MLflow UI.
  

4. **Dockerization**

   * Created Dockerfile for backend (FastAPI) + frontend (Streamlit).
   * Pinned dependencies with `requirements.txt`.

5. **Deployment on Render**

   * **FastAPI** serves REST API for predictions.
   * **Streamlit** provides an interactive web app.
   * Both deployed seamlessly via **Render**.

---

## 📂 Project Structure

```
MUSHROOM_CLASSIFICATION_PROJECT/
│
├── data/                
│   ├── raw/              # Original dataset
│   └── processed/        # Cleaned & encoded datasets
│
├── frontend/             # Streamlit frontend
│   ├── pages/            # Multi-page setup (e.g., prediction page)
│   │   └── 1_Predict.py
│   ├── utils/            # Frontend utilities
│   │   └── api_client.py
│   └── streamlit_main.py # Streamlit app entrypoint
│
├── models/               # Trained/saved models
│
├── src/                  # FastAPI backend + utilities
│   ├── api.py            # REST API entrypoint
│   ├── predict.py        # Prediction logic
│   ├── utils.py          # Helper functions
│   └── enums.py          # Enums/constants
│
├── train.py              # Training + MLflow logging
├── requirements.txt      # Dependencies
├── Dockerfile            # Docker build config
├── start.sh              # Script to launch FastAPI + Streamlit
└── README.md             # Documentation
```

---

## 🛠️ Tech Stack

* **Python 3.9**
* **scikit-learn**, **XGBoost**
* **MLflow**
* **FastAPI**
* **Streamlit**
* **Docker**
* **Render**

---

## ▶️ Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/mushroom-classification.git
   cd mushroom-classification
   ```

2. Create a virtual environment:

   ```bash
   python -m venv myenv
   myenv\Scripts\activate     
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start backend (FastAPI):

   ```bash
   uvicorn src.api:app --reload --host 0.0.0.0 --port 8000
   ```

5. Start frontend (Streamlit):

   ```bash
   streamlit run frontend/streamlit_main.py
   ```

---

## 🐳 Run with Docker

1. Build Docker image:

   ```bash
   docker build -t mushroom-classifier .
   ```

2. Run container:

   ```bash
   docker run -p 8000:8000 -p 8501:8501 mushroom-classifier
   ```

---

## 🌐 Deployment

* **Backend:** FastAPI REST API deployed on Render
* **Frontend:** Streamlit app deployed on Render
* **Containerization:** Docker ensures reproducibility

---

## 📊 Results

* Metrics & parameters logged in MLflow.
* Compared models on accuracy & F1-score.
* Streamlit app allows users to classify mushrooms as **Edible** or **Poisonous** interactively.

---

# 🍄 Mushroom Classification – ML Deployment Project

This project builds a **Mushroom Edible vs. Poisonous Classifier** using multiple machine learning models, logs experiments with **MLflow**, and deploys the final application with a **FastAPI backend** and **Streamlit frontend** inside a **Dockerized environment** on **Render**.

---

## 🚀 Project Workflow

1. **Data Preprocessing & Feature Encoding**

   * Loaded the [Kaggle Mushroom Classification Dataset](https://www.kaggle.com/uciml/mushroom-classification).
   * Handled categorical variables using label encoding.
   * Prepared training and test sets.

2. **Model Training**
   Trained 6 models and compared performance:

   * Logistic Regression
   * Decision Tree
   * Random Forest
   * Gradient Boosting
   * XGBoost
   * SVM

3. **Experiment Tracking with MLflow**

   * Logged metrics, parameters, and artifacts for all models.
   * Used MLflow UI to compare performance and select the best model.

4. **Dockerization**

   * Created a Dockerfile to containerize both backend (FastAPI) and frontend (Streamlit).
   * Ensured reproducibility with pinned dependencies (`requirements.txt`).

5. **Deployment on Render**

   * FastAPI serves the REST API for predictions.
   * Streamlit provides an interactive frontend UI.
   * Both services deployed seamlessly on **Render**.

---

## 📂 Project Structure

MUSHROOM_CLASSIFICATION_PROJECT
│── data
│   ├── processed
│   └── raw
│
│── frontend
│   ├── background
│   ├── pages
│   │   └── 1_Predict.py
│   ├── utils
│   │   └── api_client.py
│   └── streamlit_main.py
│
│── mlruns
│   
│   
│   
│
│── models
│
│── myenv
│
│── src
│   ├── __pycache__
│   ├── __init__.py
│   ├── api.py
│   ├── enums.py
│   ├── predict.py
│   └── utils.py
│
│── Dockerfile
│── README.md
│── requirements.txt
│── start.sh
└── train.py           
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

## ▶️ Running Locally

1. Clone this repo:

   ```bash
   git clone https://github.com/your-username/mushroom-classification.git
   cd mushroom-classification
   ```
2. Create and activate a virtual environment:

   ```bash
   python -m venv myenv
   myenv\Scripts\activate     
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Run backend (FastAPI):

   ```bash
   uvicorn src.api:app --reload --host 0.0.0.0 --port 8000
   ```
5. Run frontend (Streamlit):

   ```bash
   streamlit run frontend/streamlit_main.py
   ```

---

## 🐳 Running with Docker

1. Build the Docker image:

   ```bash
   docker build -t mushroom-classifier .
   ```
2. Run the container:

   ```bash
   docker run -p 8000:8000 -p 8501:8501 mushroom-classifier
   ```

---

## 🌐 Deployment

* **Backend:** FastAPI (REST API) deployed on Render
* **Frontend:** Streamlit app deployed on Render
* **Containerization:** Docker ensures consistent environment

---

## 📊 Results

* Models compared in MLflow UI
* Best model selected based on accuracy & F1 score
* Fully interactive frontend allows users to classify mushrooms as **Edible** or **Poisonous**






# 🍄 Mushroom Classification – ML Deployment Project

This project builds a **Mushroom Edible vs. Poisonous Classifier** using multiple machine learning models, tracks experiments with **MLflow**, and deploys the final application with a **FastAPI backend** and **Streamlit frontend** inside a **Dockerized environment** on **Render**.

---

## 🚀 Workflow

1. **Data Preprocessing & Feature Encoding**

   * Loaded the [Kaggle Mushroom Classification Dataset](https://www.kaggle.com/uciml/mushroom-classification).
   * Applied label encoding for categorical variables.
   * Split data into training and test sets.

2. **Model Training**
   Trained and compared 6 ML models:

   * Logistic Regression
   * Decision Tree
   * Random Forest
   * Gradient Boosting
   * XGBoost
   * SVM

3. **Experiment Tracking with MLflow**

   * Logged metrics, parameters, and artifacts.
   * Compared performance using MLflow UI.
   * Selected the best-performing model.

4. **Dockerization**

   * Dockerfile created to package backend (FastAPI) + frontend (Streamlit).
   * Dependencies pinned in `requirements.txt`.

5. **Deployment on Render**

   * **FastAPI** serves the REST API for predictions.
   * **Streamlit** provides an interactive UI.
   * Both deployed seamlessly using **Render**.

---

## 📂 Project Structure

```
MUSHROOM_CLASSIFICATION_PROJECT/
├── data/            # Datasets
├── frontend/        # Streamlit app
├── models/          # Saved models
├── src/             # FastAPI backend & utils
├── train.py         # Training + MLflow logging
├── requirements.txt # Dependencies
├── Dockerfile       # Docker config
├── start.sh         # Startup script
└── README.md        # Documentation
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
   source myenv/bin/activate   # Linux/Mac
   myenv\Scripts\activate      # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the backend (FastAPI):

   ```bash
   uvicorn src.api:app --reload --host 0.0.0.0 --port 8000
   ```

5. Start the frontend (Streamlit):

   ```bash
   streamlit run frontend/streamlit_main.py
   ```

---

## 🐳 Run with Docker

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

* **Backend:** FastAPI REST API on Render
* **Frontend:** Streamlit UI on Render
* **Containerization:** Docker ensures consistent environments

---

## 📊 Results

* All models logged in MLflow with metrics.
* Best model selected based on **Accuracy** and **F1-score**.
* Interactive frontend lets users classify mushrooms as **Edible** or **Poisonous**.

---

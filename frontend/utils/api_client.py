import requests

API_URL = "http://127.0.0.1:8000"

def predict_mushroom(features: dict, model_name: str = "random_forest") -> dict:
    """
    Send features to backend and get mushroom edibility prediction.
    """
    try:
        response = requests.post(f"{API_URL}/predict?model_name={model_name}", json=features)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.json().get("detail", "Unknown error")}
    except Exception as e:
        return {"error": str(e)}

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.predict import predict

app = FastAPI(
    title="🍄 Mushroom Classification API",
    description="Predict whether a mushroom is edible ('e') or poisonous ('p').",
    version="1.0.0",
)

class MushroomInput(BaseModel):
    cap_shape: str
    cap_surface: str
    cap_color: str
    bruises: str
    odor: str
    gill_attachment: str
    gill_spacing: str
    gill_size: str
    gill_color: str
    stalk_shape: str
    stalk_root: str
    stalk_surface_above_ring: str
    stalk_surface_below_ring: str
    stalk_color_above_ring: str
    stalk_color_below_ring: str
    veil_type: str
    veil_color: str
    ring_number: str
    ring_type: str
    spore_print_color: str
    population: str
    habitat: str

@app.get("/")
def root():
    return {"message": "Welcome to the Mushroom Classification API 🚀"}

@app.post("/predict")
def predict_mushroom(input_data: MushroomInput, model_name: str = "random_forest"):
    input_dict = input_data.dict()
    try:
        # Get prediction code ('e' or 'p')
        prediction_code = predict(input_dict, model_name=model_name)
        # Map to human-readable label
        prediction_label = "edible" if prediction_code == 'e' else "poisonous"
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction failed: {e}")
    
    return {
        "model": model_name,
        "prediction_code": prediction_code,
        "prediction_label": prediction_label
    }

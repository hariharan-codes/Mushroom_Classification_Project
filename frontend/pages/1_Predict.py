import streamlit as st
from utils.api_client import predict_mushroom
import base64
import os

# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(page_title="Mushroom Prediction", page_icon="🔮", layout="wide")

# -----------------------------
# Page title
# -----------------------------
st.title("🍄 Mushroom Edibility Prediction")
st.write("Predict whether a mushroom is **edible or poisonous** based on its physical characteristics.")

# -----------------------------
# Function to set local background image
# -----------------------------
def set_bg_local(image_file):
    if not os.path.exists(image_file):
        st.error("Background image not found!")
        return
    
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    
    st.markdown(
        f"""
        <style>
        /* Main background */
        body {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-attachment: fixed;
        }}
        /* Main app content */
        .stApp {{
            background-color: rgba(255, 255, 255, 0.1);
            padding: 2rem;
        }}
        /* Sidebar transparency */
        [data-testid="stSidebar"] {{
            background-color: rgba(0, 0, 0,1);
        }}
        /* Dropdown styling */
        div.stSelectbox > div[data-baseweb="select"] {{
            background-color: black;
            color: white;
        }}
        div.stSelectbox > div[data-baseweb="select"] span {{
            color: white;
        }}
        div.stSelectbox > div[data-baseweb="select"] svg {{
            fill: white;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# -----------------------------
# Set background image
# -----------------------------
bg_image_path = r"C:\Users\shari\Documents\Sem 3\MLops\Project\mushroom_classification_project\frontend\background\predict page.jpg"
set_bg_local(bg_image_path)

# -----------------------------
# Model selector
# -----------------------------
MODEL_OPTIONS = {
    "decision_tree": "Decision Tree",
    "random_forest": "Random Forest",
    "gradient_boosting": "Gradient Boosting",
    "logistic_regression": "Logistic Regression",
    "svm": "Support Vector Machine",
    "xgboost": "XGBoost"
}

model_name = st.selectbox(
    "Select Model", 
    list(MODEL_OPTIONS.keys()), 
    format_func=lambda x: MODEL_OPTIONS[x]
)

# -----------------------------
# Feature mappings (code → full name)
# -----------------------------
cap_shape_map = {"x": "convex", "b": "bell", "c": "conical", "f": "flat", "k": "knobbed", "s": "sunken"}
cap_surface_map = {"s": "smooth", "y": "scaly", "f": "fibrous", "g": "grooved"}
cap_color_map = {"n": "brown", "b": "buff", "c": "cinnamon", "g": "gray", "r": "green", "p": "pink", "u": "purple", "e": "red", "w": "white", "y": "yellow"}
bruises_map = {"t": "bruises", "f": "no bruises"}
odor_map = {"a": "almond", "l": "anise", "c": "creosote", "y": "fishy", "f": "foul","m": "musty", "n": "none", "p": "pungent", "s": "spicy"}
gill_attachment_map = {"a": "attached", "d": "descending", "f": "free", "n": "notched"}
gill_spacing_map = {"c": "close", "w": "crowded"}
gill_size_map = {"b": "broad", "n": "narrow"}
gill_color_map = {"k": "black", "n": "brown", "b": "buff", "h": "chocolate", "g": "gray", "r": "green", "o": "orange", "p": "pink", "u": "purple", "e": "red", "w": "white", "y": "yellow"}
stalk_shape_map = {"e": "enlarging", "t": "tapering"}
stalk_root_map = {"b": "bulbous", "c": "club", "u": "cup", "e": "equal", "z": "rooted", "r": "rhizomorphs", "?": "missing"}
stalk_surface_map = {"f": "fibrous", "y": "scaly", "k": "silky", "s": "smooth"}
stalk_color_map = {"n": "brown", "b": "buff", "c": "cinnamon", "g": "gray", "o": "orange", "p": "pink", "e": "red", "w": "white", "y": "yellow"}
veil_type_map = {"p": "partial", "u": "universal"}
veil_color_map = {"n": "brown", "o": "orange", "w": "white", "y": "yellow"}
ring_number_map = {"n": "none", "o": "one", "t": "two"}
ring_type_map = {"c": "cobwebby", "e": "evanescent", "f": "flaring", "l": "large", "n": "none", "p": "pendant", "s": "sheathing", "z": "zone"}
spore_print_color_map = {"k": "black", "n": "brown", "b": "buff", "h": "chocolate", "r": "green","o": "orange", "u": "purple", "w": "white", "y": "yellow"}
population_map = {"a": "abundant", "c": "clustered", "n": "numerous", "s": "scattered", "v": "several", "y": "solitary"}
habitat_map = {"g": "grasses", "l": "leaves", "m": "meadows", "p": "paths", "u": "urban", "w": "woods", "d": "waste"}

# -----------------------------
# Feature inputs
# -----------------------------
cap_shape = st.selectbox("Cap Shape", list(cap_shape_map.values()))
cap_surface = st.selectbox("Cap Surface", list(cap_surface_map.values()))
cap_color = st.selectbox("Cap Color", list(cap_color_map.values()))
bruises = st.selectbox("Bruises", list(bruises_map.values()))
odor = st.selectbox("Odor", list(odor_map.values()))
gill_attachment = st.selectbox("Gill Attachment", list(gill_attachment_map.values()))
gill_spacing = st.selectbox("Gill Spacing", list(gill_spacing_map.values()))
gill_size = st.selectbox("Gill Size", list(gill_size_map.values()))
gill_color = st.selectbox("Gill Color", list(gill_color_map.values()))
stalk_shape = st.selectbox("Stalk Shape", list(stalk_shape_map.values()))
stalk_root = st.selectbox("Stalk Root", list(stalk_root_map.values()))
stalk_surface_above_ring = st.selectbox("Stalk Surface Above Ring", list(stalk_surface_map.values()))
stalk_surface_below_ring = st.selectbox("Stalk Surface Below Ring", list(stalk_surface_map.values()))
stalk_color_above_ring = st.selectbox("Stalk Color Above Ring", list(stalk_color_map.values()))
stalk_color_below_ring = st.selectbox("Stalk Color Below Ring", list(stalk_color_map.values()))
veil_type = st.selectbox("Veil Type", list(veil_type_map.values()))
veil_color = st.selectbox("Veil Color", list(veil_color_map.values()))
ring_number = st.selectbox("Ring Number", list(ring_number_map.values()))
ring_type = st.selectbox("Ring Type", list(ring_type_map.values()))
spore_print_color = st.selectbox("Spore Print Color", list(spore_print_color_map.values()))
population = st.selectbox("Population", list(population_map.values()))
habitat = st.selectbox("Habitat", list(habitat_map.values()))

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict"):
    features = {
        "cap_shape": list(cap_shape_map.keys())[list(cap_shape_map.values()).index(cap_shape)],
        "cap_surface": list(cap_surface_map.keys())[list(cap_surface_map.values()).index(cap_surface)],
        "cap_color": list(cap_color_map.keys())[list(cap_color_map.values()).index(cap_color)],
        "bruises": list(bruises_map.keys())[list(bruises_map.values()).index(bruises)],
        "odor": list(odor_map.keys())[list(odor_map.values()).index(odor)],
        "gill_attachment": list(gill_attachment_map.keys())[list(gill_attachment_map.values()).index(gill_attachment)],
        "gill_spacing": list(gill_spacing_map.keys())[list(gill_spacing_map.values()).index(gill_spacing)],
        "gill_size": list(gill_size_map.keys())[list(gill_size_map.values()).index(gill_size)],
        "gill_color": list(gill_color_map.keys())[list(gill_color_map.values()).index(gill_color)],
        "stalk_shape": list(stalk_shape_map.keys())[list(stalk_shape_map.values()).index(stalk_shape)],
        "stalk_root": list(stalk_root_map.keys())[list(stalk_root_map.values()).index(stalk_root)],
        "stalk_surface_above_ring": list(stalk_surface_map.keys())[list(stalk_surface_map.values()).index(stalk_surface_above_ring)],
        "stalk_surface_below_ring": list(stalk_surface_map.keys())[list(stalk_surface_map.values()).index(stalk_surface_below_ring)],
        "stalk_color_above_ring": list(stalk_color_map.keys())[list(stalk_color_map.values()).index(stalk_color_above_ring)],
        "stalk_color_below_ring": list(stalk_color_map.keys())[list(stalk_color_map.values()).index(stalk_color_below_ring)],
        "veil_type": list(veil_type_map.keys())[list(veil_type_map.values()).index(veil_type)],
        "veil_color": list(veil_color_map.keys())[list(veil_color_map.values()).index(veil_color)],
        "ring_number": list(ring_number_map.keys())[list(ring_number_map.values()).index(ring_number)],
        "ring_type": list(ring_type_map.keys())[list(ring_type_map.values()).index(ring_type)],
        "spore_print_color": list(spore_print_color_map.keys())[list(spore_print_color_map.values()).index(spore_print_color)],
        "population": list(population_map.keys())[list(population_map.values()).index(population)],
        "habitat": list(habitat_map.keys())[list(habitat_map.values()).index(habitat)],
    }

    result = predict_mushroom(features, model_name)

    if "error" in result:
        st.error(f"❌ Error: {result['error']}")
    else:
        prediction_label = result['prediction_label'].upper()  # Capital letters
        st.success(f"Prediction: **{prediction_label}**")

import streamlit as st
import base64
import os

# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(page_title="Mushroom Classification", page_icon="🍄", layout="wide")

# -----------------------------
# Function to set local background image
# -----------------------------
def set_bg_local(image_file):
    """
    Set background image from local file
    """
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
            background-color: rgba(255, 255, 255, 0.1);  /* semi-transparent content */
            padding: 2rem;
        }}
        /* Sidebar transparency */
        [data-testid="stSidebar"] {{
            background-color: rgba(0,0,0,1);  /* semi-transparent */
        }}
        /* Optional: sidebar text color */
        [data-testid="stSidebar"] .css-1d391kg {{
            color: black;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# -----------------------------
# Set the background image
# -----------------------------
bg_image_path = r"C:\Users\shari\Documents\Sem 3\MLops\Project\mushroom_classification_project\frontend\background\predict page.jpg"
set_bg_local(bg_image_path)

# -----------------------------
# Home page content
# -----------------------------
st.title("🍄 Mushroom Classification App")
st.write("""
Welcome!  
This app predicts whether a mushroom is **edible or poisonous** based on its physical characteristics.
""")

# -----------------------------
# Instructions with image
# -----------------------------
col1, col2 = st.columns([2, 1])  # 2:1 width ratio
with col1:
    st.subheader("🔧 How it works:")
    st.write("""
1. Select the **Predict** page from the sidebar.  
2. Enter mushroom features (cap shape, surface, odor, etc.).  
3. Choose a model and click **Predict**.  
4. The system will tell you if the mushroom is edible or poisonous.
""")

with col2:
    instruction_image_path = r"C:\Users\shari\Documents\Sem 3\MLops\Project\mushroom_classification_project\frontend\background\mushroom image.png"
    if os.path.exists(instruction_image_path):
        st.image(instruction_image_path, use_container_width=True)
    else:
        st.warning("Instruction image not found!")

# -----------------------------
# Dataset link
# -----------------------------
st.write("""
You can access the original Mushroom dataset here:  
[Mushroom Dataset](https://archive.ics.uci.edu/ml/datasets/mushroom)
""")

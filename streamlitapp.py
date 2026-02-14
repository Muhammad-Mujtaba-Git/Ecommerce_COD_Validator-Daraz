import streamlit as st
import pandas as pd
import joblib
import os

# Import categories from your centralized file
# (Make sure model/categories.py exists in the same working directory)
try:
    from model.categories import categories
except ImportError:
    # Fallback just in case the import fails
    categories = [
        "Beauty & Grooming", "Women's Fashion", "Soghaat", "Appliances",
        "Home & Living", "Kids & Baby", "Men's Fashion", "Mobiles & Tablets",
        "Superstore", "Others", "Health & Sports", "Computing",
        "Entertainment", "Books", "School & Education"
    ]

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="E-commerce Fraud Predictor", page_icon="📦", layout="centered")

# --- LOAD MODEL ---
@st.cache_resource
def load_model():
    model_path = os.path.join('model', 'Daraz.pkl')
    try:
        return joblib.load(model_path)
    except FileNotFoundError:
        st.error("Model file not found! Please make sure 'model/Daraz.pkl' exists.")
        return None

model = load_model()

# --- TITLE & DESCRIPTION ---
st.title("📦 COD Order Validator")
st.markdown("""
This system predicts if a **Cash-on-Delivery (COD)** order will be **Successful (Net)** or **Cancelled (Gross)**.
It analyzes factors like *Price, Category, and Seasonality* to flag high-risk orders.
""")

st.divider()

# --- INPUT FORM ---
with st.form("prediction_form"):
    st.header("1. Order Details")
    
    col1, col2 = st.columns(2)
    with col1:
        price = st.number_input("Item Price (PKR)", min_value=1, max_value=9999999, value=2000, step=100)
    with col2:
        qty = st.number_input("Quantity", min_value=1, max_value=10, value=1)

    st.header("2. Product & Time")
    
    category = st.selectbox("Category", categories)
    
    col3, col4 = st.columns(2)
    with col3:
        month = st.slider("Month", 1, 12, 11, help="1=Jan, 12=Dec")
    with col4:
        date = st.slider("Day of Month", 1, 31, 15)

    # Submit Button
    submitted = st.form_submit_button("🔮 Predict Outcome", type="primary")

# --- PREDICTION LOGIC ---
if submitted and model:
    # 1. Create DataFrame (Strictly matches the 5 features in predict.py)
    input_df = pd.DataFrame([{
        "price": float(price),
        "qty_ordered": float(qty),
        "category_name_1": category,
        "Month": float(month),
        "date": float(date)
    }])

    # 2. Predict
    # Find exactly where 'Gross' is in the model classes to avoid hardcoding [0][1]
    gross_index = list(model.classes_).index('Gross')
    risk_score = model.predict_proba(input_df)[0][gross_index]
    
    # 3. Threshold Logic (Matched to predict.py)
    threshold = 0.30 
    is_risky = risk_score >= threshold

    # --- DISPLAY RESULTS ---
    st.divider()
    st.subheader("Prediction Results")

    if is_risky:
        st.error(f"🚨 **GROSS (High Cancellation Risk)**")
        st.write(f"This order has a **{risk_score:.1%}** chance of being cancelled.")
        st.progress(float(risk_score), text="Risk Level")
        
        # Explain WHY (Simple rules based on existing inputs)
        if month in [1, 9]:
            st.warning("💡 **Insight:** This month has historically high return/cancellation rates.")
        if qty > 5:
            st.warning("💡 **Insight:** High-quantity COD orders carry a larger cancellation risk.")
            
    else:
        st.success(f"✅ **NET (Safe Order)**")
        st.write(f"This order is safe! Risk Score: **{risk_score:.1%}**")
        st.progress(float(risk_score), text="Risk Level")

    # Debug details
    with st.expander("See Internal Data"):
        st.json({
            "Inputs": input_df.to_dict(orient="records")[0],
            "Risk Score": float(risk_score),
            "Threshold applied": threshold
        })
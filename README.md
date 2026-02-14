
# 📦 E-Commerce COD Risk Predictor 

**An End-to-End Machine Learning System to predict Cash-on-Delivery (COD) order cancellations.**

## 📌 The Business Problem
In e-commerce, Cash-on-Delivery (COD) orders carry a high risk of customer cancellation or return upon delivery, leading to significant reverse logistics costs. 

This application uses a Machine Learning model trained on transactional data to flag high-risk orders *before* they are shipped. Orders exceeding a 30% cancellation probability are flagged as 🚨 **GROSS (High Risk)**, allowing businesses to manually verify the order, while low-risk orders are marked as ✅ **NET (Safe)**.

## 🏗️ Architecture & Tech Stack
This project is built using a modern decoupled architecture:
1. **Frontend (Streamlit):** An interactive web dashboard for business users to input order details and view risk assessments.
2. **Backend API (FastAPI):** A high-performance REST API that handles data validation and serves the ML model.
3. **Machine Learning (Scikit-Learn):** A pre-trained classification pipeline that processes features and outputs probability scores.

**Tech Stack:** `Python`, `FastAPI`, `Streamlit`, `Scikit-Learn`, `Pandas`, `Pydantic`, `Docker`

---

## 🚀 Features
* **Strict Data Validation:** Uses **Pydantic** to enforce data types and constraints (e.g., preventing negative prices or invalid categories) before data reaches the model.
* **Real-Time API Inference:** FastAPI backend returns predictions and risk probability percentages instantly.
* **User-Friendly Dashboard:** Streamlit UI with sliders, dropdowns, and progress bars for intuitive risk evaluation.
* **Explainable Insights:** The UI provides dynamic warnings explaining *why* an order might be risky (e.g., high quantities or historically risky months).

---

## 📂 Project Structure
```text
├── model/
│   ├── Daraz.pkl          # Trained Scikit-Learn Model & Preprocessing Pipeline
│   ├── predict.py         # Prediction logic mapping inputs to model outputs
│   └── categories.py      # Centralized lists for Pydantic and Streamlit
├── schema/
│   └── userInput.py       # Pydantic schema for strict API input validation
├── main.py                # FastAPI backend application entry point
├── streamlitapp.py        # Streamlit frontend user interface
├── requirements.txt       # Python dependencies
└── Dockerfile             # Containerization configuration
🐳 Quick Start: Running with Docker (Recommended)
You don't need to install Python or download the code to run this app. You can pull the pre-built image directly from Docker Hub!

Pull the image from Docker Hub:

Bash
docker pull muhammadmujtabaai/daraz-cod-risk-checker
Run the container:

Bash
docker run -p 7860:7860 muhammadmujtabaai/daraz-cod-risk-checker
Open your browser and navigate to http://localhost:7860

💻 How to Run Locally (From Source)
Prerequisites
Make sure you have Python 3.9+ installed. Clone the repository and install the required packages:

Bash
pip install -r requirements.txt
Step 1: Start the FastAPI Backend
Open a terminal and start the Uvicorn server to run the API:

Bash
uvicorn main:app --reload
The API will now be running at: http://127.0.0.1:8000

View the interactive API documentation (Swagger UI) at: http://127.0.0.1:8000/docs

Step 2: Start the Streamlit Frontend
Open a second, separate terminal and run the Streamlit app:

Bash
streamlit run streamlitapp.py
The web dashboard will automatically open in your browser at http://localhost:8501.

📡 API Documentation
If you want to integrate this model into another application, you can send a POST request directly to the /predict endpoint.

Endpoint: POST /predict

Request Body (JSON):

JSON
{
  "price": 2500,
  "qty_ordered": 1,
  "category_name_1": "Men's Fashion",
  "Month": 11,
  "date": 15
}
Response (JSON):

JSON
{
  "predictions": {
    "prediction": "Net (Safe )",
    "probability_of_cancellation": "12.50%"
  }
}

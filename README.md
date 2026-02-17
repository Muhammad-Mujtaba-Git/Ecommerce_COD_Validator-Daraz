
# 📦 E-Commerce COD Risk Predictor 

**An End-to-End Machine Learning System to predict Cash-on-Delivery (COD) order cancellations.**
A Full Stack AI microservice designed to predict Cash-on-Delivery (COD) cancellation risks for the largest e-commerce dataset in Pakistan. This project moves beyond standard accuracy metrics to calculate real-world business ROI, deploying a mathematically optimized machine learning model via a fault-tolerant FastAPI and Streamlit architecture.

### Live Deployments
* **Frontend Application (Streamlit):** [Live Dashboard](https://huggingface.co/spaces/MuhammadMujtabaAIML/Daraz_COD_Validator_Streamlit)
* **Backend API (FastAPI Swagger UI):** [Live API Documentation](https://muhammadmujtabaaiml-daraz-cod-validator-fastapi.hf.space/docs)
* **Docker Image:** [Docker Hub Repository](https://hub.docker.com/r/muhammadmujtabaai/daraz-cod-risk-checker)
* **Source Code:** [GitHub Repository](https://github.com/Muhammad-Mujtaba-Git/Ecommerce_COD_Validator-Daraz)

---

## 1. The Business Problem & Solution
Cash-on-Delivery (COD) orders carry significant financial risk. When a customer refuses a delivery, the business absorbs the two-way shipping cost. 

Instead of treating this purely as a classification problem, this model simulates a **Call Center Cost Matrix**. 
* **The Strategy:** Flag high-risk orders and route them to a human call center for verification before shipping.
* **The Math:** Calling a customer costs PKR 20. Catching a cancellation saves PKR 200 in shipping.
* **The Result:** Through a custom probability threshold analysis, the model proved that setting the classification threshold to **30%** maximizes Net Profit, perfectly balancing call center expenses against saved shipping costs.

## 2. Architecture & Technologies
This application is built using a decoupled microservice architecture:

* **Machine Learning Pipeline:** Scikit-Learn, Pandas, Imbalanced-Learn
* **Backend API:** FastAPI, Uvicorn, Pydantic
* **Frontend UI:** Streamlit, Requests
* **Deployment:** Docker, Hugging Face Spaces

## 3. Key Engineering Features

**Fault-Tolerant Frontend (Graceful Degradation)**
The Streamlit application communicates with the FastAPI backend via POST requests. To prevent application freezes during server sleep cycles or API timeouts, the frontend features a 5-second timeout trap. If the live API fails, the application silently and instantly falls back to a globally loaded local `.pkl` model, ensuring zero downtime for the end user.

**Strict Data Gatekeeping**
The FastAPI backend utilizes Pydantic `BaseModel` and `@field_validator` decorators. All incoming API payloads are strictly sanitized, enforcing type checking, value constraints (e.g., maximum item limits), and case-insensitive categorical matching before the data ever reaches the inference engine. 

**Cold Start Simulation (Target Leakage Removal)**
During feature engineering, high-cardinality historical identifiers (`Customer ID`) were actively stripped from the dataset. This forces the Random Forest model to evaluate risk based purely on transaction fundamentals (Price, Category, Seasonality, Quantity), ensuring the model performs robustly on brand-new, first-time customers.

**Global Memory Management**
The Random Forest `.pkl` pipeline is loaded into global memory outside of the prediction functions. This prevents the server from reading the hard drive on every API request, reducing latency to milliseconds.

---

## 4. Local Installation & Setup

If you wish to run this architecture locally, follow the steps below.

**Prerequisites:**
* Python 3.11+
* Docker (Optional)

**Step 1: Clone the repository**

git clone [https://github.com/Muhammad-Mujtaba-Git/Ecommerce_COD_Validator-Daraz.git](https://github.com/Muhammad-Mujtaba-Git/Ecommerce_COD_Validator-Daraz.git)
cd Ecommerce_COD_Validator-Daraz


Step 2: Install dependencies

Bash


pip install -r requirements.txt


Step 3: Run the FastAPI Backend

Bash


uvicorn main:app --reload --port 8000


The API documentation will be available at http://127.0.0.1:8000/docs
Step 4: Run the Streamlit Frontend
Open a new terminal window and run:

Bash


streamlit run streamlitapp.py


Run via Docker
To pull and run the fully containerized API directly from Docker Hub:

Bash


docker pull muhammadmujtabaai/daraz-cod-risk-checker
docker run -p 7860:7860 muhammadmujtabaai/daraz-cod-risk-checker






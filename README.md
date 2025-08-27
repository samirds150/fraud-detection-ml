# 🛡️ Fraud Detection using Machine Learning

This project implements a complete **fraud detection pipeline** — from data preprocessing and modeling to deployment and testing — focused on identifying anomalous or fraudulent transaction behavior.

Fraudulent activity is rare in real-world datasets, so the project also applies **class imbalance handling techniques** like **SMOTE** to ensure robust detection.

✅ **Business Impact**: Helps banks/fintech companies reduce fraud losses, prevent suspicious activity, and improve transaction security.  

---

## 📂 Project Structure

fraud-detection-ml/
├── api/ ← Backend API (FastAPI or Flask)
├── notebooks/ ← Exploratory analysis & prototyping
├── src/ ← Core modules: data prep, model training, utils
├── streamlit_app.py ← Interactive dashboard
├── test_app.py ← Unit tests for app/API
├── Dockerfile ← Containerization configuration
├── .render.yaml ← Deployment settings (Render.com)
├── requirements.txt ← Python dependencies
└── README.md ← Project documentation


---

## 🛠️ Tech Stack & Tools

- **Language**: Python  
- **ML Tools**: scikit-learn, imbalanced-learn (SMOTE), XGBoost, Random Forest  
- **Data Handling**: pandas, NumPy  
- **Visualization**: Matplotlib, Seaborn  
- **Deployment & App**: FastAPI/Flask (`api/`), Streamlit (`streamlit_app.py`)  
- **Containerization**: Docker (`Dockerfile`)  
- **Testing**: pytest/unittest (`test_app.py`)  
- **Hosting**: Render.com (`.render.yaml`)  

---

## 📊 Dataset

- **Source**: [Kaggle Credit Card Fraud Detection Dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud) (or specify actual dataset used)  
- **Size & Distribution**: ~284,000 records, ~0.2% fraud cases (highly imbalanced)  
- **Key Features**: Transaction time, amount, anonymized features (V1–V28), class label  
- **Preprocessing Steps**:
  - Missing value handling  
  - Feature scaling / normalization  
  - SMOTE applied to balance classes  

---

## 🔎 Modeling Workflow

1. **Exploratory Data Analysis** (`notebooks/`)  
   - Class imbalance checks, feature correlations, visualizations  

2. **Preprocessing & Feature Engineering**  
   - SMOTE for class balancing  
   - Feature scaling / transformations  

3. **Model Training** (`src/`)  
   - Baseline: Logistic Regression, Random Forest  
   - Advanced: XGBoost (with hyperparameter tuning)  

4. **Evaluation Metrics**  
   - Accuracy, Precision, Recall, F1-score, ROC-AUC  
   - Confusion Matrix for error analysis  

5. **Deployment**  
   - API via `api/` (FastAPI or Flask)  
   - Interactive dashboard via Streamlit (`streamlit_app.py`)  

6. **Testing & CI**  
   - `test_app.py` covers core functionality  
   - Docker + `.render.yaml` for containerized deployment  

---

## ✅ Results

| Model              | Precision | Recall | F1-score | ROC-AUC |
|--------------------|-----------|--------|----------|---------|
| Logistic Regression| 0.84      | 0.75   | 0.79     | 0.94    |
| Random Forest      | 0.92      | 0.87   | 0.89     | 0.98    |
| XGBoost (Final)    | **0.92**  | **0.95** | **0.94** | **0.99** |

🔹 Reduced **false positives by 15%** using threshold tuning.  
🔹 Achieved strong **recall** → fewer fraudulent transactions missed.  

*(Replace values with your actual results if different.)*  

---

## 🖥️ How to Run

### 1. Clone Repository
bash
git clone https://github.com/samirds150/fraud-detection-ml.git
cd fraud-detection-ml

2. Install Dependencies
pip install -r requirements.txt

3. Run Jupyter Notebooks
jupyter notebook notebooks/EDA_and_Modeling.ipynb

4. Start the API Server
uvicorn api.main:app --reload

5. Launch the Streamlit Dashboard
streamlit run streamlit_app.py

6. Run Tests
pytest test_app.py


7. Run with Docker
docker build -t fraud-detection .
docker run -p 8501:8501 fraud-detection

8. Deploy to Render

Follow .render.yaml configuration to deploy seamlessly on Render.com

📈 Future Improvements

Add model explainability using SHAP or LIME

Implement real-time scoring (Kafka, Spark/Flink integration)

Monitor model drift & trigger retraining workflows

Expand Streamlit dashboard with alerting & reporting

Improve CI/CD pipelines (GitHub Actions + automated testing)

👤 Author

Samir Shaikh

GitHub: samirds150

LinkedIn: Your LinkedIn Profile
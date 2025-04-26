# 🏡 Real Estate Forecasting Platform

**Predict and analyze Toronto's housing market trends with Azure, FastAPI, FAISS, and Power BI.**

---

## 📖 About the Project

This project builds a complete real estate forecasting pipeline:

- **Price Prediction** using XGBoost regression models
- **Similarity Search** with FAISS vector databases
- **Azure Blob & SQL Database** for cloud storage and querying
- **FastAPI Server** to serve predictions and nearest neighbor results
- **Power BI Dashboard** for interactive visualizations

Built for a modern AI-Cloud-BI ecosystem. 🚀

---

### 📑 data_exploration.ipynb
🔎 **Initial exploratory analysis:**
- Load the Toronto real estate dataset
- Visualize key features (Home Price Index trends)
- Check for missing values and understand data types
---

## 📂 Project Structure

```plaintext
RealEstate-Forecasting-Platform/
├── azure/
│   ├── upload_to_blob.py          # Upload files to Azure Blob Storage
│   └── azure_sql_connector.py     # Upload dataset to Azure SQL Database
├── api/
│   └── app.py                     # FastAPI prediction and similarity API
├── data/
│   └── processed_toronto_hpi.csv   # Preprocessed dataset
├── model/
│   ├── price_model.pkl            # XGBoost price prediction model
│   └── vector_index.faiss         # FAISS vector similarity index
├── notebooks/
│   ├── data_exploration.ipynb       # Data exploration
│   ├── preprocessing_data.ipynb     # Data cleaning and feature engineering
│   ├── price_prediction_model.ipynb # Model training and evaluation
│   └── vector_similarity_search.ipynb # FAISS similarity search
├── powerbi/
│   └── real_estate_dashboard.pbix   # Power BI dashboard
├── requirements.txt
└── README.md
```

---

## 📚 Notebooks Overview

### 📑 data_exploration.ipynb
🔎 **Initial exploratory analysis:**
- Load the Toronto real estate dataset
- Visualize key features (Home Price Index trends)
- Check for missing values and understand data types

### 📑 preprocessing_data.ipynb
🧹 **Data cleaning & preprocessing:**
- Handle missing values
- Extract useful features (Year, Month)
- Save the processed dataset for modeling

### 📑 price_prediction_model.ipynb
🎯 **Model training & evaluation:**
- Train XGBoost regression model to predict Home Price Index (HPI)
- Evaluate model performance (RMSE, R²)
- Save the trained model (`price_model.pkl`)

### 📑 vector_similarity_search.ipynb
🧠 **FAISS-based similarity search:**
- Create vector embeddings
- Build FAISS index for fast nearest neighbor search
- Save the FAISS vector index (`vector_index.faiss`)

---

## 🏗️ System Architecture

```plaintext
[Kaggle Dataset] → [Preprocessing] → [Model Training]
       ↓                     ↓
[Azure Blob Storage]     [Azure SQL Database]
       ↓                     ↓
    [FAISS Index]         [Power BI Dashboard]
       ↓                     ↓
       [FastAPI Prediction & Similarity API]
```

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/RealEstate-Forecasting-Platform.git
cd RealEstate-Forecasting-Platform
```

### 2. Install requirements
```bash
pip install -r requirements.txt
```

### 3. Run FastAPI server
```bash
uvicorn api.app:app --reload
```

- **Predict Price Endpoint:**
  ```bash
  POST http://127.0.0.1:8000/predict
  ```
- **Find Similar Properties Endpoint:**
  ```bash
  POST http://127.0.0.1:8000/similar
  ```

### 4. Upload Data to Azure (optional)
Run scripts:
```bash
python azure/upload_to_blob.py
python azure/azure_sql_connector.py
```

### 5. Power BI Dashboard
- Connect Power BI to Azure SQL.
- Load and visualize real estate trends.

---

## 🛠️ Tech Stack

| Tool/Framework       | Purpose                         |
|----------------------|---------------------------------|
| Python               | Main programming language      |
| Pandas / NumPy       | Data manipulation               |
| XGBoost              | Price prediction model          |
| FAISS                | Similarity search engine        |
| FastAPI              | API deployment                  |
| Azure Blob Storage   | Cloud file storage              |
| Azure SQL Database   | Cloud relational storage        |
| Power BI             | Data visualization              |

---

## ✨ Author

Made with ❤️ by [Narges vahdani](https://github.com/nargesghv)

---

✅ **This project demonstrates full real-world AI, Cloud, and BI integration.**
✅ **Ready for professional portfolio, CV, LinkedIn, and recruiters!**

---

> _Feel free to fork, star ⭐, and collaborate!_ 🚀

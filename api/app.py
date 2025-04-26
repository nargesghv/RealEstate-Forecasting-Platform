from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import faiss

app = FastAPI(title="Toronto Real Estate Prediction API")

model = joblib.load("../model/price_model.pkl")
faiss_index = faiss.read_index("../model/vector_index.faiss")

class PredictionRequest(BaseModel):
    year: int
    month: int

@app.post("/predict")
def predict_price(req: PredictionRequest):
    input_data = np.array([[req.year, req.month]])
    prediction = model.predict(input_data)
    return {"predicted_price_index": prediction[0]}

@app.post("/similar")
def find_similar(req: PredictionRequest):
    input_vector = np.array([[req.year, req.month]]).astype('float32')
    _, indices = faiss_index.search(input_vector, k=5)
    return {"similar_properties_indices": indices.tolist()[0]}
